# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import time
import openai
import pytesseract
import requests
import telebot
from PIL import Image
from tools import *
# useful for handling different item types with a single interface


class AlphaplanPipeline:
    def process_item(self, item, spider):
        return item


class TweetPipeline(object):
    def __init__(self):
        super().__init__()

    def process_item(self, item, spider):
        print('处理item')
        if re.findall(r'\blaunch|sale|release|live|list|发射|fire|available|time|liquidity|contract|address|stealth|airdrop', item['tweet_text'], re.I):
            if item['tweet_media']:
                res = requests.get(item['tweet_media'], stream=True)
                with open('alpha.png', 'wb') as file:
                    # 每128个流遍历一次
                    for data in res.iter_content(128):
                        # 把流写入到文件，这个文件最后写入完成就是，selenium.png
                        file.write(data)  # data相当于一块一块数据写入到我们的图片文件中
                media_text = pytesseract.image_to_string(Image.open('alpha.png'), lang='chi_sim+eng')
            else:
                media_text = ''
            tweet_text = item['tweet_text'] + '\n' + media_text

            msg = [{"role": "assistant", "content":"sale:%Y-%m-%d %H:%M:%S %Z,launch:%Y-%m-%d %H:%M:%S %Z"},{"role": "user","content": '当前时间'+time.strftime('%Y-%m-%d %H:%M:%S %Z')+'\n'+tweet_text + '按照之前的格式提取以上内容中代币sale时间/代币launch时间'}]

            hf = chatGPT(msg)
            item['tweet_gpt'] = hf
            # print(len(re.findall(r'unknown', hf, re.I)))
            alpha_time=re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+)|(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} 中国标准时间)', hf)
            if alpha_time:
                item['alpha_time'] = alpha_time.group()
                bot.send_message(-980470620,
                                 '['+item['tweet_user']+']'+'(https://twitter\.com/'+item['tweet_user']+')'+' @['+item['tweet_alpha']+']'+'(https://twitter\.com/'+item['tweet_alpha']+')  \|  [' + item['alpha_time'].replace('-','\-') +']'+'(https://twitter\.com/'+ item['tweet_user']+ '/status/' + item['tweet_id']+')\n\n'+'`'+item['tweet_text']+'`',parse_mode="MarkdownV2",disable_web_page_preview=False)
                item.save()
            # print(tweet_text, hf, sep='\n')
            # 发送消息
            # producer.send('alpha', str('@' + item['tweet_user'] + '\n' + hf + '\n详见以下推文https://twitter.com/' + item[
            #                          'tweet_user'] + '/status/' + item['tweet_id'] + '\n' + item['tweet_text']).encode('utf-8'))

        print('处理完毕',item,sep='\n')

        return item








