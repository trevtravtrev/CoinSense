# CryptoPortfolioTracker
Simple CLI tool to track your cryptocurrency portfolio in real time.

![](demo.gif)

##Fun stuff:  
- Python Version: 3.7  
- Supported Operating Systems: Windows 10  
- Currently only supports Binance Smart Chain Tokens (can add Ethereum Blockchain support upon request)
- Updates prices in real-time (5-10x per second)
- Supports ALL Binance Smart Chain Tokens INCLUDING new and unlisted coins


##To Use:  
- `pip install -r requirements.txt`
- enter your coins in config.py
- run cryptoportfoliotracker.py (or edit and run cryptoportfoliotracker.bat)

##Warnings:
- Be sure to press CTRL+C before terminating the command line interface. Reasoning is due to this app using selenium which in turn opens headless background firefox processes that ONLY get terminated if CTRL+C is pressed before closing the app.
- Pressing CTRL+C to safely terminate this app will close ALL running firefox processes. This includes closing your personal open firefox windows (if firefox is your browser of choice and you have windows open while terminating this app).
- Use at your own risk. This project was created for educational purposes only. I hereby do not take responsibility for misuse or abuse of this application in any way by those who use, modify, or redistribute it.