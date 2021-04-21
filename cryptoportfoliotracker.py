from os import getcwd, path, system
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import config
import cli
from coin import Coin


def get_coins():
    """
    Creates coin objects for each coin entered in config.py and returns a list containing all coin objects
    :return: coins (list of coin objects)
    """
    coins = []
    for key in config.portfolio:
        coin = Coin()
        coin.set_contract(key)
        coin.set_quantity(config.portfolio.get(key))
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
    return f'{coin.price * coin.quantity:.2f}'


def terminate():
    """
    Kill all running firefox processes.
    """
    system("taskkill /im firefox.exe /f")
    print("Sucessfully terminated all Firefox processes.\nSafe to exit. ")


def main():
    """
    Main loop. Dynamically creates, searches, updates, and prints pricing 5-10 times per second to command line.
    """
    coins = None
    try:
        cli._cls()
        print("Gathering coin data... this might take a few seconds.")
        print("\n\n\n\n\n\n\n\n\n\nPress CTRL+C to terminate safely.")
        base_url = "https://charts.bogged.finance/?token="
        coins = get_coins()
        # coin actions that only need to run once
        for coin in coins:
            coin.set_driver(get_driver())
            coin.driver.get(base_url + coin.contract)

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
                    except Exception as e:
                        print(e)
                        continue
            cli.print_data(coins)
            print("\n\n\nPress CTRL+C to terminate safely.")
    except KeyboardInterrupt:
        terminate()


if __name__ == '__main__':
    main()
