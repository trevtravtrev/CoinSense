import pandas as pd
import os
from tabulate import tabulate


def print_data(coins):
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
        coin_data_dict["Balance"].append(coin.balance)
    # convert coin_data_dictionary to pandas dataframe
    df = pd.DataFrame(coin_data_dict)
    _cls()
    return print(tabulate(df, headers='keys', tablefmt='psql'))


def _cls():
    os.system('cls' if os.name=='nt' else 'clear')
