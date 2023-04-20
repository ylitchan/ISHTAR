import datetime
import schedule
import time
from tools import *
from alphaApp.models import AlphaInfo

def do_task():
    print(datetime.datetime.now())
    # 这里是要执行的事务
    #bot.send_message(-1001982993052, '\n'.join(['UST DAO',time.strftime('%Y-%m-%d'),"🚀Today's Alpha"]))
    alpha1=AlphaInfo.objects.filter(alpha_time__icontains=time.strftime('%Y-%m-%d')).values('tweet_alpha','alpha_time','tweet_user','tweet_id','tweet_text')
    alpha2 = set()
    alpha = []
    for i in alpha1:
        if i['tweet_alpha'] not in alpha2:
            alpha.append(i)
            alpha2.add(i['tweet_alpha'])
    bot.send_message(-1001982993052, '\n\n'.join([time.strftime('%Y-%m-%d').replace('-','\-'),"🚀Today's Alpha"]+['['+i['tweet_user']+']'+'(https://twitter\.com/'+i['tweet_user']+')'+' @['+i['tweet_alpha']+']'+'(https://twitter\.com/'+i['tweet_alpha']+')  \|  [' + i['alpha_time'].replace('-', '\-') +']'+'(https://twitter\.com/'+ i['tweet_user']+ '/status/' + i['tweet_id']+')' for i in alpha]),parse_mode="MarkdownV2",disable_web_page_preview=False)
# 设置每天的 8 点执行任务
schedule.every().day.at("08:00").do(do_task)

while True:
    schedule.run_pending()
    time.sleep(60)