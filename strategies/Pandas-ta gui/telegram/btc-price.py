import requests
from datetime  import datetime
import telebot
from secret import token

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usdt")
    responce = req.json()
    sell_price = responce['btc_usdt']['sell']
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot (token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет Падруга хочешь узнать цену на биткойна? набери тогда слово price")


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usdt")
                responce = req.json()
                sell_price = responce['btc_usdt']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Something went wrong'
                )
        else:
            bot.send_message(message.chat.id, 'ВВЕДИ СЛОВО price')

    bot.polling()  # прослушивает обновления и сообщения, поступающие через API Telegram
if __name__ == '__main__':
    # get_data()
    telegram_bot(token)