import os
import requests
import telebot

ISHTARider_tg = telebot.TeleBot(os.environ.get("ISHTARider_tg"))

a = requests.get('http://ishtar.freehk.svipss.top/alpha/launching')
print(666666666, a.text)

