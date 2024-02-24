import requests
from datetime  import datetime
import telebot
from secret import token
from tickers import tickers, tickers_str
# word = 'null'
# def get_data():
#     req = requests.get(f"https://yobit.net/api/3/ticker/{word}_usdt")
#     responce = req.json()
#     sell_price = responce[f'{word}_usdt']['sell']
#     print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot (token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hi, enter any cryptocurrency ticker such as btc/xrp, or any other you like. \nIf you don\'t know what tickers exist, write \'tickers\'.")


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == '?':
            bot.send_message(
                message.chat.id,
                f"Just copy and paste needed ticker \n {tickers_str}")

        elif len(message.text.lower()) <= 6:
            # global word
            symbol = message.text
            try:
                req = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT")
                responce = req.json()
                sell_price = responce['price']
                #sell_price = responce[f'{symbol}_usdt']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell {(symbol.upper())} price: {sell_price} \nIf you want to see full list of tickers enter \'?\'"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Try correct crypto ticker \nIf you don\'t know what tickers exist, write \'?\'.'
                )
        else:
            bot.send_message(message.chat.id, 'Use only commands with tickers, \nIf you don\'t know what tickers exist, write \'?\'.')

    bot.polling()  # прослушивает обновления и сообщения, поступающие через API Telegram
if __name__ == '__main__':
    # get_data()
    telegram_bot(token)