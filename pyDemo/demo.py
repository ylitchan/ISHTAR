import os
import requests
import telebot

ISHTARider_tg = telebot.TeleBot(os.environ.get("ISHTARider_tg")).send_message(-1001982993052,'66666666666')

a = requests.get('http://ishtar.freehk.svipss.top/alpha/launching')
print(666666666, a.text)

