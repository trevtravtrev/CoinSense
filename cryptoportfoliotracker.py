import cli

from bs4 import BeautifulSoup  # type: ignore
from os import getcwd, path, system
from selenium import webdriver  # type: ignore
from selenium.webdriver.firefox.options import Options  # type: ignore
from selenium.webdriver.firefox.webdriver import WebDriver  # type: ignore
from typing import List

from coin import Coin
from config import CFG


def get_coins() -> List[Coin]:
    """
    Creates coin objects for each coin entered in config.py and returns a list containing all coin objects
    :return: coins (list of coin objects)
    """
    coins: List[Coin] = []

    for portfolio in CFG.portfolios:
        for con in portfolio.contracts:
            coin = Coin()
            coin.coin_type = portfolio.name
            coin.contract = con.contract
            coin.quantity = con.quantity
            coin.set_tracker_url(portfolio.tracker)
            coins.append(coin)
    return coins


def get_driver() -> WebDriver:
    """
    Finds file path of geckodriver.exe and creates selenium driver
    :return: driver
    """
    gecko_path = path.join(getcwd(), "driver", CFG.driver)
    options: Options = Options()
    if CFG.headless:
        options.add_argument("--headless")  # type: ignore
    driver = webdriver.Firefox(options=options, executable_path=gecko_path)
    return driver


def get_symbol(page_data: BeautifulSoup):
    """
    Extract the coin's symbol from the page's title
    :param page_data: webpage data parsed by beautiful soup
    :return: token symbol
    """
    title: str = page_data.title.string  # type: ignore
    symbol = title.split("$")[0].replace(" ", "")
    return symbol


def get_price(page_data: BeautifulSoup) -> float:
    """
    Extract the coin's price from the page's title
    :param page_data: webpage data parsed by beautiful soup
    :return: coin price
    """
    title: str = page_data.title.string  # type: ignore
    return float(title.split("$")[1].split(" ")[0].replace("$", ""))


def get_balance(coin: Coin) -> float:
    """
    Calculate your coin balance based off quantity and price
    :param coin: coin object
    :return: coin balance
    """
    return float(f"{coin.price * coin.quantity:.2f}")


def terminate() -> None:
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
        cli._cls()  # type: ignore
        print("Gathering coin data... this might take a minute.")
        print("Press CTRL+C at any time to terminate safely.")
        coins = get_coins()
        num_browsers = len(coins)
        # coin actions that only need to run once
        for coin in coins:
            print(f"{num_browsers} browser(s) left to open...")
            coin.driver = get_driver()
            coin.driver.get(coin.tracker_url)  # type:ignore
            num_browsers -= 1

        # coin actions that update in infinite loop
        while True:
            for coin in coins:
                # update each coin's dynamic data
                while True:
                    # check if browser is loaded
                    try:
                        page_data = BeautifulSoup(coin.driver.page_source, "html.parser")  # type:ignore
                        coin.symbol = get_symbol(page_data)
                        coin.price = get_price(page_data)
                        coin.balance = get_balance(coin)
                        break
                    # try again if browser not loaded
                    except KeyboardInterrupt:
                        terminate()
                    except:
                        continue
            cli.print_data(coins)  # type: ignore
            print("\n\n\nPress CTRL+C to terminate safely.")
    except KeyboardInterrupt:
        terminate()


if __name__ == "__main__":
    main()
