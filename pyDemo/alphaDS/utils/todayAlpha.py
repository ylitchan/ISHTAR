import telebot
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alphaDS.settings') # 替换成您的项目名
django.setup()
from alphaApp.models import AlphaInfo
import schedule
import time
bot = telebot.TeleBot("6291256191:AAExAaaagpZgEAdBvhOMRN2JxlXr8om4qJA")

def do_task():
    # 这里是要执行的事务
    b=AlphaInfo.objects.filter(tweet_id='Alice')
    print(b)
    bot.send_message(-1001982993052, 'niha666666')

# 设置每天的 8 点执行任务
schedule.every().day.at("16:28").do(do_task)

while True:
    schedule.run_pending()
    time.sleep(60)