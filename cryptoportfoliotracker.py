import threading
import logging
from os import getcwd, path, system
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from user_agent import generate_user_agent
from random import randint

import config
import cli
from coin import Coin


def get_coins():
    """
    Creates coin objects for each coin entered in config.py and returns a list containing all coin objects
    :return: coins (list of coin objects)
    """
    coins = []
    for key in config.bsc_portfolio:
        coin = Coin()
        coin.set_coin_type("bsc")
        coin.set_contract(key)
        coin.set_quantity(config.bsc_portfolio.get(key))
        coin.set_tracker_url()
        coins.append(coin)
    for key in config.eth_portfolio:
        coin = Coin()
        coin.set_coin_type("eth")
        coin.set_contract(key)
        coin.set_quantity(config.eth_portfolio.get(key))
        coin.set_tracker_url()
        coins.append(coin)
    return coins


def get_proxies():
    """
    Gets a list of proxies and returns them
    :return: proxy list
    """
    req_proxy = RequestProxy()
    req_proxy.logger.disabled = True
    return req_proxy.get_proxy_list()


def get_driver(proxy=None):
    """
    Finds file path of geckodriver.exe and creates selenium driver
    :return: driver
    """
    gecko_path = path.join(getcwd(), "driver", "geckodriver.exe")
    if config.firefox_profile_path:
        profile = webdriver.FirefoxProfile(config.firefox_profile_path)
    else:
        profile = webdriver.FirefoxProfile()
    if config.use_random_user_agent:
        profile.set_preference("general.useragent.override", generate_user_agent())
    options = Options()
    if config.headless:
        options.add_argument('--headless')
    if proxy:
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        firefox_capabilities['proxy'] = {
            "proxyType": "MANUAL",
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy
        }
        driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=gecko_path, capabilities=firefox_capabilities)
    else:
        driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=gecko_path)
    return driver


def get_symbol(coin, page_data):
    """
    Extract the coin's symbol from the page's title
    :param page_data: webpage data parsed by beautiful soup
    :return: token symbol
    """
    title = page_data.title.string
    if coin.coin_type == "bsc":
        symbol = title.split('$')[0].replace(' ', '')
    elif coin.coin_type == "eth":
        symbol = title.split(' ')[1].replace(' ', '')
    return symbol


def get_price(page_data):
    """
    Extract the coin's price from the page's title
    :param page_data: webpage data parsed by beautiful soup
    :return: coin price
    """
    title = page_data.title.string
    price = float(title.split('$')[1].split(' ')[0].replace('$', ''))
    return price


def get_balance(coin):
    """
    Calculate your coin balance based off quantity and price
    :param coin: coin object
    :return: coin balance
    """
    return float(f'{coin.price * coin.quantity:.2f}')


def terminate():
    """
    Kill all running firefox processes.
    """
    system("taskkill /im firefox.exe /f")
    print("\nSuccessfully terminated all Firefox processes.\nSafe to exit.")


def print_logo():
    return print("""
  ___  ____  _  _  ____  ____  __  
 / __)(  _ \( \/ )(  _ \(_  _)/  \ 
( (__  )   / )  /  ) __/  )( (  O )
 \___)(__\_)(__/  (__)   (__) \__/ 
 ____   __  ____  ____  ____  __   __    __  __  
(  _ \ /  \(  _ \(_  _)(  __)/  \ (  )  (  )/  \ 
 ) __/(  O ))   /  )(   ) _)(  O )/ (_/\ )((  O )
(__)   \__/(__\_) (__) (__)  \__/ \____/(__)\__/ 
 ____  ____   __    ___  __ _  ____  ____ 
(_  _)(  _ \ / _\  / __)(  / )(  __)(  _ \\
  )(   )   //    \( (__  )  (  ) _)  )   /
 (__) (__\_)\_/\_/ \___)(__\_)(____)(__\_)
        """)


def _open_tracker(coin, proxy=None):
    """
    Spawn driver and open browser webpage for a coin tracker.
    :param coin: coin object
    """
    coin.set_driver(get_driver(proxy))
    coin.driver.get(coin.tracker_url)


def main():
    """
    Main loop. Dynamically creates, searches, updates, and prints pricing 5-10 times per second to command line.
    """
    coins = None
    thread_list = []
    # globally disable logging because the http_request_randomizer library has un-configurable logging
    logging.disable(logging.CRITICAL)
    try:
        cli._cls()
        print_logo()
        print("Press CTRL+C at any time to terminate safely.\n")
        coins = get_coins()
        num_coins = len(coins)
        print(f'\nOpening {num_coins} coin trackers...')
        if config.use_proxies:
            # get proxies
            proxies = get_proxies()
        # open coin tracking urls in separate browsers
        for coin in coins:
            if config.use_proxies:
                # grab random proxy from list and remove it from list
                random_proxy = proxies[randint(0, len(proxies)-1)]
                proxies.remove(random_proxy)
                proxy = random_proxy.get_address()
                # threaded implementation to open trackers
                thread = threading.Thread(target=_open_tracker, args=(coin, proxy))
            else:
                thread = threading.Thread(target=_open_tracker, args=(coin,))
            thread.start()
            thread_list.append(thread)
            if config.ddos_bypass and coin.coin_type == "eth":
                sleep(config.ddos_sleep)
        # wait for all threads to complete
        for thread in thread_list:
            thread.join()
            num_coins -= 1
            print(f'{num_coins} remaining...')
        print("\nGathering coin data...")
        # coin actions that update in infinite loop
        while True:
            for coin in coins:
                # update each coin's dynamic data
                while True:
                    # check if browser is loaded
                    try:
                        page_data = BeautifulSoup(coin.driver.page_source, 'html.parser')
                        coin.set_symbol(get_symbol(coin, page_data))
                        coin.set_price(get_price(page_data))
                        coin.set_balance(get_balance(coin))
                        break
                    # try again if browser not loaded
                    except KeyboardInterrupt:
                        terminate()
                    except:
                        continue
            cli.print_data(coins)
            print("\n\n\nPress CTRL+C to terminate safely.")
            sleep(config.refresh_time)
    except KeyboardInterrupt:
        terminate()


if __name__ == '__main__':
    main()
