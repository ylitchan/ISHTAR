# -*- encoding=utf8 -*-
__author__ = "颜立全"

import time

import requests

import telebot
import openai

openai.api_key = "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"
bot = telebot.TeleBot("6291256191:AAExAaaagpZgEAdBvhOMRN2JxlXr8om4qJA")
all = {}


def floor(slug):
    nft = requests.get('https://app.nfttrack.ai/api/search?q=' + slug).json()['data']['collections'][0]['opensea_slug']
    res = requests.get('https://app.nfttrack.ai/api/collection_info/' + nft)
    return nft + '地板：' + str(res.json()['data']['floor_price'])


def chatGPT(msg: list):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
        # messages=[
        #     {"role": "user", "content": "未成年人不应该浏览哪些网址，列举20个"},
        # ]
    )
    return u"%s" % res['choices'][0]['message']['content']


@bot.message_handler(commands=['/g'],func=lambda message: True)
def echo_all(message):
    if '/gpt' in message.text:
        print(message.text)
        id = message.from_user.id
        log = all.get(id, [])
        log.append({"role": "user", "content": message.text.replace('/gpt','')})
        print(log)
        hf = chatGPT(log)
        all[id] = [{"role": "user", "content": message.text}, {"role": "assistant", "content": hf}]
        bot.send_message(message.chat.id, hf)
        print(all)
    # try:
    #     name=message.from_user.first_name +message.from_user.last_name
    #
    # except:
    #     name=message.from_user.first_name
    # try:
    #     reply = '\nreply2:\n'+message.reply_to_message.text
    # except:
    #     reply=''
    # json = {
    #     "msgtype": "text",
    #     "text": {
    #         "content": name+ ':\n' + message.text+reply,
    #     }
    # }
    # requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=dc326a08-1641-4d78-b5ac-24f143ae7449',
    #               json=json)

    # print(name+ ':\t' + message.text)


bot.infinity_polling()
