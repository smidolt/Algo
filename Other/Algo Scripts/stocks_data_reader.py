import pandas as pd
import yfinance

ticker = yfinance.Ticker('TSLA')

stocks = ticker.history(period='1y')

print(stocks)