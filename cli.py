import pandas as pd
import os
from tabulate import tabulate


def print_data(coins):
    total = 0
    coin_data_dict = {
        'Token': [],
        'Price': [],
        'Quantity': [],
        'Balance': []
    }
    # add each coin's data to the coin_data_dictionary
    for coin in coins:
        coin_data_dict["Token"].append(coin.symbol)
        coin_data_dict["Price"].append(coin.price)
        coin_data_dict["Quantity"].append(coin.quantity)
        coin_data_dict["Balance"].append(f'${coin.balance}')
        total += float(coin.balance)
    # add total as last row in CLI
    coin_data_dict["Token"].append("TOTAL")
    coin_data_dict["Price"].append("-")
    coin_data_dict["Quantity"].append("-")
    coin_data_dict["Balance"].append(f'${total:.2f}')
    # convert coin_data_dictionary to pandas dataframe
    df = pd.DataFrame(coin_data_dict)
    _cls()
    return print(tabulate(df, headers='keys', tablefmt='fancy_grid'))


def _cls():
    os.system('cls' if os.name == 'nt' else 'clear')
