import pandas as pd
import pandas_ta as ta
import ccxt
import requests
from secret import WEB_HOOK_URL

#print(ccxt.exchanges) # print a list of all available exchange classes

exchange = ccxt.binance()
bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
ema = ta.ema(close= df['close'], length=200)
adx = df.ta.adx()
rsi = df.ta.rsi()
df = pd.concat([df, ema, adx, rsi],axis=1)

last_row = df. iloc[-1] #ILOC - полезная функция позволяющая дать данные по определенной ячейке!
print(last_row)
if last_row ['ADX_14'] >= 25:
    message = f"STRONG TREND: The ADX is {last_row['ADX_14']}"
    print (message)
    if last_row['EMA_200'] >= last_row['close']:
        message= f"EMA 200: is {last_row['EMA_200'] } we're above the 200-day ema."
       # print(f"close price is {last_row['open']}")
        payload = {
            'username': 'alert-bot',
            'content': message
        }

        requests.post(WEB_HOOK_URL, payload)
    elif last_row['EMA_200'] <= last_row['close']:
        messageema = f"EMA 200: is {last_row['EMA_200']} we're below the 200-day ema. "
        print(messageema)
        print (f"close price is: {last_row['close']}")
        payload = {
            'username': 'alert-bot',
            'content': f'hi guys {messageema}'
        }

        requests.post(WEB_HOOK_URL, payload)
if last_row ['ADX_14'] < 25:
    message = f"WEAK TREND: The ADX is {last_row['ADX_14']:.2f}"#:.2f to round to 2 decimal
    print(message)
    if last_row['EMA_200'] >= last_row['close']:
        message = f"EMA 200: is {last_row['EMA_200']}"
        print(message)
    #a = 10.1234
    #f'{a:.2f}'
        payload = {
            'username': 'alert-bot',
            'content': message
        }
    elif last_row['EMA_200'] <= last_row['close']:
        messageema = f"EMA 200: is {last_row['EMA_200']} we're below the 200-day ema. "
        print(messageema)
        print(f"close price is: {last_row['close']}")
        payload = {
            'username': 'alert-bot',
            'content': f'hi guys {messageema}'
        }

        requests.post(WEB_HOOK_URL, payload)

#print(df)
#df.to_csv('newdata.csv', index=False)