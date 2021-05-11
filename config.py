"""
Crypto Portfolio Tracker Settings Configuration File

bsc_portfolio: a binance smart chain coin dictionary {contract:quantity} where "contract" is the token's contract address string and "quantity" is an int for the quantity you own
eth_portfolio: a ethereum blockchain coin dictionary {contract:quantity} where "contract" is the token's contract address string and "quantity" is an int for the quantity you own
headless: a bool parameter that sets whether the selenium background coin tracking firefox processes will be visible to user or not (suggested: True)
use_proxies: a bool parameter that sets whether or not a unique proxy will be used for each coin tracking browser to get around DDOS protection. Buggy (suggested: False)
ddos_bypass: a bool parameter that bypasses coin tracking website ddos protectors with the trade off of longer initial load time upon launch (suggested: True)
refresh_time: an int number that sets the refresh time for updating prices. Higher time uses less CPU (suggested: 1-5 seconds)
"""

# tracked by bogged.finance charts (make sure the contract addresses are trackable on the website)
bsc_portfolio = {
    "0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3": 100000000,
    "0xd27d3f7f329d93d897612e413f207a4dbe8bf799": 100000000,
    "0x2170Ed0880ac9A755fd29B2688956BD959F933F8": 1,
    "0x87ffc48c9f89fc5dfa05836e083406d684fd6331": 100000000,
    "0xfaFf5251EA98f90540D6BacDf7A458f61b456C06": 100000000
}

# tracked by dextools.io charts (make sure the contract addresses are trackable on the website)
eth_portfolio = {
    "0xc0067d751fb1172dbab1fa003efe214ee8f419b6": 2000,
    "0x7fd1de95fc975fbbd8be260525758549ec477960": 1000000
}

headless = True

firefox_profile_path = r"path\to\your\firefox\profile"

use_random_user_agent = True

use_proxies = False

ddos_bypass = True

refresh_time = 5
