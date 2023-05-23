import os
import requests
import telebot

ISHTARider_tg = telebot.TeleBot(os.environ.get("ISHTARider_tg"))
ISHTARider_tg.send_message(-980470620, 'msg')
while True:
    try:
        a = requests.get('https://www.api.foxe.vip/api/merkle/0xbb4c9679861244E4074383A7F865443C08C7C7b1', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'})
        print(666666666, a.text)
        ISHTARider_tg.send_message(-1001982993052, a.text)
        break
    except:
        print(555555)
        continue
