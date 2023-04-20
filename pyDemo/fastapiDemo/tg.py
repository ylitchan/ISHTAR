import asyncio
import json
import random
import re

import openai
import requests
import tweepy
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
import uvicorn
import telebot
from kafka import KafkaProducer, KafkaConsumer

# 创建生产者实例
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])



app = FastAPI()
bot = telebot.TeleBot("6291256191:AAExAaaagpZgEAdBvhOMRN2JxlXr8om4qJA")
bearer_token = "AAAAAAAAAAAAAAAAAAAAACpGmgEAAAAAgc7ia5UBBMhSt4QF7vUYXFrrC1M%3DZv76NCELvLybMQNvLycj4kptMVkYpuo7sgYkjJ8RnFTgHPDBx0"
client = tweepy.Client('AAAAAAAAAAAAAAAAAAAAAPEGjQEAAAAAREb6WuXu7rNwm8ChnkpJoSJmSkw%3DXgtd6IlBg9SyrAcVhTOVucCrYL4OGfSjjCmMbfM8mFTi3CqUcL')
openai.api_key = "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"
# with open(r'.\history.json', 'a+') as js:
#     all = json.load(js)
#     print('====================',len(all),all)
all = set()


async def chatGPT(msg: list):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
        # messages=[
        #     {"role": "user", "content": "未成年人不应该浏览哪些网址，列举20个"},
        # ]
    )
    return u"%s" % res['choices'][0]['message']['content']

async def add_member(userId):
    headers = {
        'cookie': 'des_opt_in=Y; _gcl_au=1.1.116267149.1676257589; g_state={"i_l":4,"i_p":1681369247236}; _ga_BYKEBDM7DS=GS1.1.1679899771.1.1.1679899844.0.0.0; _gid=GA1.2.1222660834.1680783998; at_check=true; mbox=PC#5d50de66cc054e10bf959bf00d0b670c.38_0#1744731433|session#db24585874f049b1b132445cb93bebc8#1681488493; _ga=GA1.2.1915858432.1679573193; kdt=2RNumTWyrbgn13h0nBHx95uYSPlUa6qMK390ud8K; _ga_34PHSZMC42=GS1.1.1681533194.15.0.1681533194.0.0.0; dnt=1; auth_multi="1568898000654680064:17e8044520b62a806dc73e68c70a019d1918e70f"; auth_token=614cb847793f6b268a64e8cf6ea05479d38bb67d; guest_id_ads=v1:168153922613435906; guest_id_marketing=v1:168153922613435906; lang=en; guest_id=v1:168153922613435906; twid=u=1573326306661793792; ct0=5bb87294748eabc856cd95ffc52dad00c7ef7abe56a299feebef81091739e80961b2842233a9a2222093250ad0270f0aedcb49afaeded4e26fa13092ad22b2cda67ba9a6ddc4ef96c139e351f9cbcaaa; personalization_id="v1_A5Cjem2NxpnAPzInu7PDFA=="',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
        'x-csrf-token': '5bb87294748eabc856cd95ffc52dad00c7ef7abe56a299feebef81091739e80961b2842233a9a2222093250ad0270f0aedcb49afaeded4e26fa13092ad22b2cda67ba9a6ddc4ef96c139e351f9cbcaaa'
        }
    var = {
        "variables": {
            "listId": "1646881802609655808",
            "userId": userId
        },
        "features": {
            "blue_business_profile_image_shape_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True
        },
        "queryId": "x0smnIS1jLLXToRYg70g4Q"
    }
    res = requests.post('https://twitter.com/i/api/graphql/x0smnIS1jLLXToRYg70g4Q/ListAddMember', headers=headers,
                      json=var)
    print(res)

@app.post("/")
async def root(json=Body(None)):
    return {"challenge": json["challenge"]}
    print('=================')
    text = json.get('message', {}).get('text', '')
    chat_id = json.get('message', {}).get('chat', {}).get('id', 0)
    if chat_id==5341501065 or chat_id==5865410419:
        print(text)
        a=re.findall(r'@.*?\n',text)
        for i in a:
            try:
                user_id=client.get_user(username=i.replace('\n','').replace('@','')).data.id
                print(user_id)
                # a=client.add_list_member(id=1639838455760035840,user_id=user_id)
                # print(a)
                # all.add(user_id)
                # 发送消息
                print(str(user_id).encode('utf-8'))
                producer.send('test', str(user_id).encode('utf-8'))
                #client.add_list_member(id=1639838455760035840,user_id=user_id)
            except:
                continue

@app.post("/ishtar")
async def events(json=Body(None)):
    print('===================================')
    print(json)

    # if "challenge" in data:
    #     # Respond to the Slack challenge
    #     return {"challenge": data["challenge"]}
    #
    # # Handle other Slack events here
    # # ...

    return {"message": "Received Slack event"}


        # text = json.get('text', '')
    # if text:
    #     hf = await chatGPT([{"role": "user", "content": text}])
    #     return JSONResponse(content=hf)
    # return


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
