import pandas as pd
import pandas_ta as ta
import ccxt, yfinance


print(ccxt.exchanges) # print a list of all available exchange classes

exchange = ccxt.binance()
bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
ema = ta.ema(close= df['close'], length=200)
print(ema)
print(df)
df = df.ta.ema(close= df['close'], length=200)
print(df)
#df.to_csv('Biodata.csv', index=False)