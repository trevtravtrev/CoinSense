from selenium.webdriver.firefox.webdriver import WebDriver #type: ignore

class Coin:
    """
    Custom coin data structure class that holds coin data and allows set access for each variable from outside functions
    """
    tracker_url: str
    coin_type: str
    contract: str
    quantity: int
    driver: WebDriver
    symbol: str
    price: float
    balance: float

    def set_tracker_url(self, url: str):
        self.tracker_url = f"{url}{self.contract}"
