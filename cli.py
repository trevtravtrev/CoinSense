import pandas as pd
import os
from tabulate import tabulate


def print_data(coins):
    """
    Prints a beautiful table of all coin data to command line interface
    :param coins: list of all coin objects
    :return: print table
    """
    total = 0
    coin_data_dict = {"Token": [], "Price": [], "Quantity": [], "Balance": []}
    # add each coin's data to the coin_data_dictionary
    for coin in coins:
        coin_data_dict["Token"].append(coin.symbol)
        coin_data_dict["Price"].append(coin.price)
        coin_data_dict["Quantity"].append(coin.quantity)
        coin_data_dict["Balance"].append(coin.balance)
        total += coin.balance
    # convert coin_data_dictionary to pandas dataframe
    df = pd.DataFrame(coin_data_dict)
    # sort by descending balance (high -> low)
    df = df.sort_values(by=["Balance"], ascending=False)
    # add TOTAL row to end of dataframe
    total_dict = {"Token": "TOTAL", "Price": "-", "Quantity": "-", "Balance": total}
    df = df.append(total_dict, ignore_index=True)
    # format Balance column with dollar sign, commas, and 2 floating points after decimal
    df["Balance"] = df.apply(lambda x: "${:,.2f}".format(x["Balance"]), axis=1)
    _cls()
    return print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))


def _cls():
    """
    Clears command line terminal
    """
    return os.system("cls" if os.name == "nt" else "clear")
