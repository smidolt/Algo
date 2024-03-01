import requests
from datetime import datetime
import telebot
import schedule
import time
import pandas as pd
import pandas_ta as ta
import ccxt
from secret import crossover1, id
from threading import Thread

def get_last_row():
    exchange = ccxt.binance()
    bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='1m', limit=5)  # Данные за последние 5 минут
    df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
    ema = ta.ema(close=df['close'], length=5)  # 5-минутная EMA
    df = pd.concat([df, ema], axis=1)
    return df.iloc[-1]

def send_telegram_message(message):
    bot = telebot.TeleBot(crossover1)
    bot.send_message(chat_id, message)

def check_ema_condition(last_row):
    if last_row['EMA_5'] >= last_row['close']:  # Проверка, если цена ниже или равна 5-минутной EMA
        return f"EMA 5: is {last_row['EMA_5']} we're above or equal to the 5-minute EMA."
    elif last_row['EMA_5'] < last_row['close']:  # Проверка, если цена выше 5-минутной EMA
        return f"EMA 5: is {last_row['EMA_5']} we're below the 5-minute EMA."

def job():
    try:
        last_row = get_last_row()
        ema_message = check_ema_condition(last_row)
        send_telegram_message(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price: {last_row['close']}\n{ema_message}")
    except Exception as ex:
        print("Error occurred:", ex)

def telegram_bot():
    bot = telebot.TeleBot(crossover1)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hi, enter any cryptocurrency ticker in any register such as \'btc\', or any other you like.")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == '?':
            bot.send_message(message.chat.id, "Just copy and paste needed ticker.")
        elif len(message.text) <= 6:
            symbol = message.text.upper()
            try:
                req = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT")
                response = req.json()
                sell_price = response['price']
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell {symbol.upper()} price: {sell_price}")
            except Exception as ex:
                bot.send_message(message.chat.id, 'Try correct crypto ticker.')
        else:
            bot.send_message(message.chat.id, 'Use only commands with tickers.')

    bot.polling()

if __name__ == '__main__':
    chat_id = id # Ваш ID чата

    # Запуск потока для телеграм-бота
    telegram_thread = Thread(target=telegram_bot)
    telegram_thread.start()

    # Запуск задачи проверки цены/EMA
    schedule.every(5).seconds.do(job)  # Проверка каждые 5 секунд
    while True:
        schedule.run_pending()
        time.sleep(1)
