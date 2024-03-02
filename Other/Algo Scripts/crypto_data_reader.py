import pandas as pd
import ccxt

print(ccxt.exchanges) # print a list of all available exchange classes
exchange = ccxt. binance()
bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
print(df)