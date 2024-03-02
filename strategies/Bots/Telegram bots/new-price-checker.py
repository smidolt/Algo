import requests
from datetime  import datetime
import telebot
from secret import token
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
        bot.send_message(message.chat.id, "Hi, enter any cryptocurrency ticker such as btc/xrp, or any other you like.")


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if len(message.text.lower()) <= 6:
            # global word
            word = message.text
            try:
                req = requests.get(f"https://yobit.net/api/3/ticker/{word}_usdt")
                responce = req.json()
                sell_price = responce[f'{word}_usdt']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell {(word.upper())} price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Try correct crypto ticker'
                )
        else:
            bot.send_message(message.chat.id, 'Use only commands with tickers')

    bot.polling()  # прослушивает обновления и сообщения, поступающие через API Telegram
if __name__ == '__main__':
    # get_data()
    telegram_bot(token)