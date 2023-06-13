class Coin:
    """
    Custom coin data structure class that holds coin data and allows set access for each variable from outside functions
    """

    bsc_url = "https://charts.bogged.finance/?token="
    eth_url = "https://dex.guru/token/"

    def __init__(self):
        self.tracker_url = None
        self.coin_type = None
        self.contract = None
        self.quantity = None
        self.driver = None
        self.symbol = None
        self.price = None
        self.balance = None

    def set_tracker_url(self):
        if self.coin_type == "eth":
            self.tracker_url = Coin.eth_url + self.contract
        elif self.coin_type == "bsc":
            self.tracker_url = Coin.bsc_url + self.contract
        else:
            raise Exception("set_tracker_url error: Invalid coin_type.")

    def set_coin_type(self, coin_type):
        self.coin_type = coin_type

    def set_contract(self, contract):
        self.contract = contract

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_driver(self, browser):
        self.driver = browser

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_price(self, price):
        self.price = price

    def set_balance(self, balance):
        self.balance = balance
