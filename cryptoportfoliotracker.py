from os import getcwd, path
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

import config
from coin import Coin


def get_coins():
    coins = []
    for key in config.portfolio:
        coin = Coin()
        coin.set_contract(key)
        coin.set_quantity(config.portfolio.get(key))
        coins.append(coin)
    return coins


def get_gecko_driver():
    gecko_path = path.join(getcwd(), "driver", "geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path=gecko_path, options=options)
    return driver


def get_browser(coin, driver):
    base_url = "charts.bogged.finance/?token="
    full_url = base_url + coin.contract
    return driver.get(full_url)


def get_symbol(page_data):
    return page_data.find("span", id="tokenSymbol")


def get_price(page_data):
    return page_data.find("span", id="price_num")


def get_balance(coin):
    return f'{coin.price * coin.quantity:.2f}'


def print_debug_data(coin):
    print(f"""
Symbol: {coin.symbol}
Quantity: {coin.quantity}
Price: {coin.price}
Balance: {coin.balance}
""")


def main():
    coins = get_coins()
    driver = get_gecko_driver()
    # coin actions that only need to run once
    for coin in coins:
        coin.set_browser(get_browser(coin, driver))
        page_data = BeautifulSoup(coin.browser.page_source)
        coin.set_symbol(get_symbol(page_data))
    # coin actions that update in infinite loop
    while True:
        for coin in coins:
            # update each coin's dynamic data
            while True:
                # check if browser is loaded
                try:
                    page_data = BeautifulSoup(coin.browser.page_source)
                    coin.set_price(get_price(page_data))
                    coin.set_balance(get_balance(coin))
                    print_debug_data(coin)
                    break
                # try again if browser not loaded
                except:
                    continue
        sleep(config.update_time)


if __name__ == '__main__':
    main()
