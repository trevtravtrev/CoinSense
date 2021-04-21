from os import getcwd, path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import config
import cli
from coin import Coin


def get_coins():
    coins = []
    for key in config.portfolio:
        coin = Coin()
        coin.set_contract(key)
        coin.set_quantity(config.portfolio.get(key))
        coins.append(coin)
    return coins


def get_driver():
    gecko_path = path.join(getcwd(), "driver", "geckodriver.exe")
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options, executable_path=gecko_path)
    return driver


def get_symbol(page_data):
    return page_data.find("span", id="tokenSymbol").get_text()


def get_price(page_data):
    price = page_data.find("span", id="price_num").get_text()
    price = float(price.replace("$", ''))
    return price


def get_balance(coin):
    return f'{coin.price * coin.quantity:.2f}'


def main():
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
                except:
                    continue
        cli.print_data(coins)

if __name__ == '__main__':
    main()
