"""
Crypto Portfolio Tracker Settings Configuration File

bsc_portfolio: a binance smart chain coin dictionary {contract:quantity} where "contract" is the token's contract address string and "quantity" is an int for the quantity you own
eth_portfolio: a ethereum blockchain coin dictionary {contract:quantity} where "contract" is the token's contract address string and "quantity" is an int for the quantity you own
headless: a bool parameter that sets whether the selenium background coin tracking firefox processes will be visible to user or not (suggested: True)
"""

from typing import List


class Contract:
    def __init__(self, contract: str, quantity: int):
        self.contract = contract
        self.quantity = quantity

    def __repr__(self):
        return f"<Contract (contract={self.contract}, quantity={self.quantity})>"


class Portfolio:
    def __init__(self, name: str, contracts: List[Contract], tracker: str):
        self.name = name
        self.contracts = contracts
        self.tracker = tracker

    def __repr__(self):
        return f"<Portfolio (name={self.name}, contracts={self.contracts}, tracker={self.tracker})>"


class Config:
    def __init__(self, headless: bool, portfolios: List[Portfolio], driver: str):
        self.headless = headless
        self.driver = driver
        self.portfolios = portfolios

    def __repr__(self):
        return f"<Config (headless={self.headless}, portfolios={self.portfolios})>"


portfolios = [
    (
        "bsc",
        [  # tracked by bogged.finance charts (make sure the contract addresses are trackable on the website)
            ("0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3", 1000000),
            ("0xd27d3f7f329d93d897612e413f207a4dbe8bf799", 1000000),
            ("0x2170Ed0880ac9A755fd29B2688956BD959F933F8", 1),
            ("0x87ffc48c9f89fc5dfa05836e083406d684fd6331", 1000000),
            ("0xfaFf5251EA98f90540D6BacDf7A458f61b456C06", 1000000),
        ],
        "https://charts.bogged.finance/?token=",
    ),
    (
        "eth",
        [  # tracked by dextools.io charts (make sure the contract addresses are trackable on the website)
            ("0xc0067d751fb1172dbab1fa003efe214ee8f419b6", 2000),
            ("0x7fd1de95fc975fbbd8be260525758549ec477960", 1000000),
        ],
        "https://www.dextools.io/app/uniswap/pair-explorer/",
    ),
]

CFG = Config(True, [], "geckodriver.exe")

for pf in portfolios:
    portfolio = Portfolio(pf[0], [Contract(ctr[0], ctr[1]) for ctr in pf[1]], pf[2])
    CFG.portfolios.append(portfolio)
