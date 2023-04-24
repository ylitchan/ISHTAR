import os
import openai
import telebot
import tweepy
from kafka import KafkaProducer, KafkaConsumer
import django
from dateutil import parser
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alphaDS.settings')  # 替换成您的项目名
django.setup()
from alphaApp.models import AlphaInfo

openai.api_key = os.environ.get('openai')
# 创建生产者实例
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


def chatGPT(msg: list):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    return u"%s" % res['choices'][0]['message']['content']


bot = telebot.TeleBot(os.environ.get("telebot"))
ISHTAR=telebot.TeleBot(os.environ.get("ISHTAR"))
client = tweepy.Client(os.environ.get("tweetapi"))

