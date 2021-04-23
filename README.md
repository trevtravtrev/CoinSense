# CryptoPortfolioTracker
Simple CLI tool to track your cryptocurrency portfolio in real time.

![](demo.gif)

## Fun stuff:  
- Python Version: 3.7  
- Supported Operating Systems: Windows 10
- Supported Coins: ALL binance smart chain coins, ALL ethereum blockchain coins, and most other popular coins  
- Updates prices in real-time (5-10x per second)



## To Use:  
- install firefox if not already installed (https://www.mozilla.org/en-US/firefox/new/)
- `pip install -r requirements.txt`
- enter your coins in config.py
- run cryptoportfoliotracker.py (or edit and run cryptoportfoliotracker.bat)

## Warnings:
- Be sure to press CTRL+C before terminating the command line interface. Reasoning is due to this app using selenium which in turn opens headless background firefox processes that ONLY get terminated if CTRL+C is pressed before closing the app.
- Pressing CTRL+C to safely terminate this app will close ALL running firefox processes. This includes closing your personal open firefox windows (if firefox is your browser of choice and you have windows open while terminating this app).
- Use at your own risk. This project was created for educational purposes only. I hereby do not take responsibility for misuse or abuse of this application in any way by those who use, modify, or redistribute it.