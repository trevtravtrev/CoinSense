"""
Crypto Portfolio Tracker settings configuration file

portfolio: a dictionary {contract:quantity} where "contract" is the token's contract string and "quantity" is an int for the quantity you own
headless: a bool parameter that sets whether the selenium background coin tracking firefox processes will be visible to user or not (suggested: True)
"""

portfolio = {
    "0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3": 1000000,
    "0xd27d3f7f329d93d897612e413f207a4dbe8bf799": 1000000
}

headless = True
