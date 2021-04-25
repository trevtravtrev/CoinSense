import threading
from os import getcwd, path, system
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep

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


def get_driver():
    """
    Finds file path of geckodriver.exe and creates selenium driver
    :return: driver
    """
    gecko_path = path.join(getcwd(), "driver", "geckodriver.exe")
    options = Options()
    if config.headless:
        options.add_argument('--headless')
    driver = webdriver.Firefox(options=options, executable_path=gecko_path)
    return driver


def get_symbol(page_data):
    """
    Extract the coin's symbol from the page's title
    :param page_data: webpage data parsed by beautiful soup
    :return: token symbol
    """
    title = page_data.title.string
    symbol = title.split('$')[0].replace(' ', '')
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
    print("Sucessfully terminated all Firefox processes.\nSafe to exit. ")


def _open_tracker(coin):
    """
    Spawn driver and open browser webpage for a coin tracker.
    :param coin: coin object
    """
    coin.set_driver(get_driver())
    coin.driver.get(coin.tracker_url)


def main():
    """
    Main loop. Dynamically creates, searches, updates, and prints pricing 5-10 times per second to command line.
    """
    coins = None
    thread_list = []
    try:
        cli._cls()
        print("======= Welcome to Crypto Portfolio Tracker =======")
        print("Press CTRL+C at any time to terminate safely.\n")
        print("Starting... this might take a minute.")
        coins = get_coins()
        num_coins = len(coins)
        print(f'\nOpening {num_coins} coin trackers...')
        # coin actions that only need to run once
        # open coin tracking urls in separate browsers
        for coin in coins:
            thread = threading.Thread(target=_open_tracker, args=(coin,))
            thread.start()
            thread_list.append(thread)
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
                        coin.set_symbol(get_symbol(page_data))
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
            sleep(1)
    except KeyboardInterrupt:
        terminate()


if __name__ == '__main__':
    main()
