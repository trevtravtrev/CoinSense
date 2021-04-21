class Coin:
    """
    Custom coin data structure class that holds coin data and allows set access for each variable from outside functions
    """
    def __init__(self):
        self.contract = None
        self.quantity = None
        self.driver = None
        self.symbol = None
        self.price = None
        self.balance = None

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
