class Coin:
    def __init__(self):
        self.contract = None
        self.quantity = None
        self.browser = None
        self.symbol = None
        self.price = None
        self.balance = None

    def set_contract(self, contract):
        self.contract = contract

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_browser(self, browser):
        self.browser = browser

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_price(self, price):
        self.price = price

    def set_balance(self, balance):
        self.balance = balance
