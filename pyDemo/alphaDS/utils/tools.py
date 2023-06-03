import re
import time
import moviepy.editor as mpe
import openai
import requests
from dateutil import parser
from jsonpath_ng import parse
from slack_sdk import WebClient
import telebot
import tweepy
import queue
import speech_recognition as sr
import redis
from alphaPlan.items import *

# 消息生产者
# q_add = queue.Queue()
# q_alpha = queue.Queue()
producer = redis.Redis(host='localhost', port=6379)
appid = os.getenv('AppID')
secret = os.getenv('AppSecret')
ISHTARider_tg = telebot.TeleBot(os.environ.get("ISHTARider_tg"))
ISHTAR_slack = WebClient(os.getenv('ISHTAR_slack'))
ISHTARider_slack = WebClient(os.getenv('ISHTARider_slack'))
CHANNEL_ID = "C052ZB95CQP"
openai.api_key = os.environ.get('openai')
bot = telebot.TeleBot(os.environ.get("telebot"))
client_tweet = tweepy.Client(os.environ.get("tweetapi"))
# admin = KafkaClient(bootstrap_servers=['localhost:9092'],api_version=(0,10,2))
# admin.add_topic("ISHTAR")
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,2))
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# chrome_driver_path = r'D:\allProjects\pyDemo\msedgedriver.exe'
# options = webdriver.EdgeOptions()
# options.add_argument(r"user-data-dir=D:\allProjects\pyDemo\edge")
# options.add_argument(r"headless")
# driver = webdriver.Edge(executable_path=chrome_driver_path, options=options, )
# #
# driver.get('https://tools.miku.ac/anime_tts/')  # 打开百度首页
# wait = WebDriverWait(driver, 30)
# wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
# # driver.implicitly_wait(10)
# input = driver.find_element(by=By.TAG_NAME, value='textarea')
# button = driver.find_element(by=By.XPATH,
#                              value='//*[@id="__layout"]/div/main/div[@class="anime_tts view"]/div[@class="nya-container pt"]/button')

hf_list = ['无限制AI']
session = requests.session()


def add_member(q_add: queue.Queue):
    member = client_tweet.get_list_members('1639838455760035840').data
    if member:
        already = [i.id for i in member]
    else:
        already = []
    while True:
        new_follow = q_add.get(block=True)
        # 發送添加到列表的請求
        if new_follow.id not in already:
            token = session.post('https://alpha-admin.ipfszj.com/api/admin/base/open/login',
                                 json={'username': 'autoadd', 'password': '123456'}).json().get(
                'data').get(
                'token')
            session.post(url='http://alpha-admin.ipfszj.com/api/admin/alpha/alpha/add',
                         headers={'Authorization': token},
                         json={'username': new_follow.username, 'bio': new_follow.description,
                               'profileImageUrl': new_follow.profile_image_url,
                               'createdAt': new_follow.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                               'followersCount': new_follow.public_metrics.get('followers_count', ''),
                               'followingCount': new_follow.public_metrics.get('following_count', ''),
                               'tweetCount': new_follow.public_metrics.get('tweet_count', ''),
                               'listedCount': new_follow.public_metrics.get('listed_count', '')})
            session.post('https://twitter.com/i/api/graphql/27lfFOrDygiZs382QLttKA/ListAddMember', json={
                "variables": {
                    "listId": "1639838455760035840",
                    "userId": new_follow.id
                },
                "features": {
                    "rweb_lists_timeline_redesign_enabled": False,
                    "blue_business_profile_image_shape_enabled": True,
                    "responsive_web_graphql_exclude_directive_enabled": True,
                    "verified_phone_label_enabled": False,
                    "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                    "responsive_web_graphql_timeline_navigation_enabled": True
                },
                "queryId": "27lfFOrDygiZs382QLttKA"
            }, headers={
                'x-csrf-token': 'aa3383f5de290543f2d112d2159d2d69160f153d32f8648852183d816487a844e6023170c0b10bc4bade97f1d2226c0e2ea8239e071aedcdfd2296453fc75b6864b1736c00d28661f3a02de16091e056',
                'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                'cookie': 'des_opt_in=Y; g_state={"i_l":4,"i_p":1685978878538}; kdt=Q5t5PoYbZC7V30BrYCwKZzsSt3b612JIMJtmb0pQ; _gcl_au=1.1.2086328013.1685102825; _ga=GA1.2.1852869831.1685180820; _gid=GA1.2.579029748.1685180820; dnt=1; ads_prefs="HBESAAA="; auth_multi="1577862800952930305:864329745d15cc0b8407f8b403bb9c80e88ace79"; auth_token=cf79681343ca5b964ab4fa004c5d9fca2bdce7a9; guest_id=v1:168528420580517298; ct0=aa3383f5de290543f2d112d2159d2d69160f153d32f8648852183d816487a844e6023170c0b10bc4bade97f1d2226c0e2ea8239e071aedcdfd2296453fc75b6864b1736c00d28661f3a02de16091e056; lang=zh-cn; twid=u=1568898000654680064; guest_id_marketing=v1:168528420580517298; guest_id_ads=v1:168528420580517298; personalization_id="v1_M+fBTWkwbZBZWjHzsW7W+w=="',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'})
            # 添加失败重新放入队列
            if new_follow.id not in [i.id for i in client_tweet.get_list_members('1639838455760035840').data]:
                print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加失败,重新放入队列')
                q_add.put(new_follow.id)
                # producer.publish('tg_add', user_id)
                time.sleep(3600)
            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加成功,计入已添加')
                already.append(new_follow.id)
                time.sleep(10)


# ts_msg = {}
# new_ts = {}

# 獲取slack中消息列標識,用文本作為鍵
def get_ts(val):
    consumer = producer.pubsub()
    consumer.subscribe(val)
    for m in consumer.listen():
        try:
            return m.get('data').decode('utf-8')
        except:
            continue
    # while True:
    #     try:
    #         for key, value in new_ts.items():
    #             if val == value:
    #                 new_ts.pop(key)
    #                 return key
    #     except:
    #         continue


# 微信小程序openid的獲取
def get_openid(data):
    code = parse('$..code').find(data)[0].value
    res = session.get(
        'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
            appid, secret, code))
    return parse('$..openid').find(res.json())[0].value


# c給hatgpt發消息
def chat_gpt(msg: list):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=msg
        )
        return {'code': 200, 'data': {'hf': u"%s" % parse('$..content').find(res)[0].value}, 'msg': 'gpt返回结果'}
    except:
        return {'code': 400, 'data': {'hf': 'gpt error'}, 'msg': '小福吃竹子去了,请稍后再来'}


# def genshin(text: str):
#     print('开始合成原神语音', text)
#     res = requests.post('https://api.okmiku.com/anime_tts', headers=headers, json={
#         "text": text,
#         "speaker": "派蒙",
#         "source": "原神",
#         "speed": 1,
#         "model": "genshin",
#         "language": "ZH",
#         "cleaned": False,
#         "noisew": 0.8,
#         "noise": 0.667})
#     if res.status_code == 200:
#         print('原神语音完成')
#         return parse('$..data').find(res.json())[0].value
#     else:
#         print('原神语音合成失败')
#         raise Exception('合成失败')


# def ISHTAR(data):
#     file_id = parse('$..file_id').find(data)
#     # chat_id=parse('$..chat.id').find(data)[0].value
#     # ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID, text='chat_id:' + str(chat_id), as_user=True,
#     #                               thread_ts='1682605196.796199')
#     if file_id:
#         print('收到tg语音消息')
#         file_id = file_id[0].value
#         # print(file_id)
#         file_url = ISHTAR_tg.get_file_url(file_id)
#         response = requests.get(file_url).content
#         with open('input.oga', 'wb') as f:
#             f.write(response)
#         audioclip = mpe.AudioFileClip("input.oga")
#         audioclip.write_audiofile("output.wav")
#         r = sr.Recognizer()
#         with sr.AudioFile('output.wav') as source:
#             # 将语音文件读取为AudioData对象
#             audio_data = r.record(source)
#         # 使用Google Speech Recognition进行识别
#         response = r.recognize_google(audio_data, language='zh-CN')
#         print('识别语音消息', response)
#     else:
#         response = parse('$..text').find(data)[0].value
#         print('收到tg消息', response)
#     # producer.send('ISHTAR', response)
#
#     ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID, text="<@U053SG7AC01> " + response, as_user=True,
#                                   thread_ts='1682605196.796199')
#     print('发送消息到slack', response)
# 處理ISHTAR作為用戶接收的消息
def ISHTAR(request):
    data = request.data
    text = parse('$..text').find(data)[0].value
    # 過濾無用信息
    if '_Typing…_' not in text and '&gt; _' not in text and '_Oops' not in text:
        print('收到slack消息', text)
        thread_ts = parse('$..thread_ts').find(data)
        # print(thread_ts)
        channel = parse('$..channel').find(data)[0].value
        bot_id = parse('$..bot_id').find(data)
        # 判斷是否首個消息沒有ts
        if channel == 'C052ZB95CQP' and not thread_ts:
            ts = parse('$..ts').find(data)[0].value
            producer.publish(text, ts)
            # new_ts[ts] = text
            # ts_msg[ts] = []
            print('首条消息,新建thread_ts')
        # 喊单处理的ts
        elif thread_ts and thread_ts[0].value == '1684548507.820999' and bot_id[0].value == 'B0543J2N27J':
            tweet_id = re.search('@\d+', text).group().replace('@', '')
            producer.publish(tweet_id, text)
            print('添加新消息到tweet_id')
        # 將claude的消息發到對應的redis頻道
        elif channel == 'C052ZB95CQP' and bot_id[0].value == 'B0543J2N27J':
            producer.publish(thread_ts[0].value, text)
            # ts_msg[thread_ts[0].value].insert(0, text)
            print('添加新消息到thread_ts')


# 處理ISHTARider作為app接收的消息
def ISHTARider(request):
    data = request.data
    bot_id = parse('$..bot_id').find(data)
    # 過濾自己的回復
    if not bot_id:
        text = parse('$..text').find(data)[0].value
        print('处理GPT项目消息', text)
        channel = parse('$..channel').find(data)[0].value
        hf = parse('$..hf').find(
            chat_gpt([{"role": "assistant", "content": hf_list[0]}, {"role": "user", "content": text}]))[0].value
        print('回复消息到ISHTARider', hf)
        ISHTARider_slack.chat_postMessage(channel=channel, text=hf)
        # requests.post('https://hooks.slack.com/services/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',
        #               json={'text': hf}, timeout=10)
        hf_list[0] = hf


# 處理alphaPlan發過來的item
def process_item(key, tweet_text, item):
    print('处理' + item.__class__.__name__)
    tweet_tag = None
    # 根據不同的類型用不同的方法
    if not isinstance(key, list) and not item['tweet_text'].startswith('RT @'):
        ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID,
                                      text="<@U053SG7AC01> " + '只需回答内容中看好的或者推荐的代币(前面加$)以及推文id(前面加@),不要分析过程。要是没有就直接给推文id(前面加@)\n' + '@' +
                                           item['tweet_id'] + ':\n' + tweet_text,
                                      as_user=True,
                                      thread_ts='1684548507.820999')
        print('claude正在分析文本', key.group())
        consumer = producer.pubsub()
        consumer.subscribe(item['tweet_id'])
        # consumer.get_message().get('data')
        for m in consumer.listen():
            hf = m.get('data')
            if isinstance(hf, int):
                continue
            hf = hf.decode('utf-8')
            break
        print('claude返回结果', hf)
        item['tweet_ai'] = hf
        tweet_tag = set(re.findall('\$[A-Za-z]+', hf, re.I))
        item['tweet_tag'] = ' \| '.join(tweet_tag)
        # for m in consumer.listen():
        #     try:
        #         hf = m.get('data').decode('utf-8')
        #         print('获取到claude回复', hf)
        #         item['tweet_gpt'] = hf
        #         tweet_tag = set(re.findall('\$[A-Za-z0-9_]+', hf, re.I))
        #         item['tweet_tag'] = ' \| '.join(tweet_tag)
        #         break
        #     except:
        #         continue
    elif isinstance(key, list):
        # 有dc鏈接就發送
        if item['tweet_alpha'] == 'discord':
            # 把鏈接從key中拿掉,避免影響後面的launch判斷
            for i in key:
                if 'https://t.co/' in i:
                    key.remove(i)
                    msg = '[' + item['tweet_user'] + ']' + '(https://twitter\.com/' + item[
                        'tweet_user'] + ')' + ' @[' + item[
                              'tweet_alpha'] + ']' + '(https://twitter\.com/' + item[
                              'tweet_alpha'] + ')  \|  [discord]' + '(https://twitter\.com/' + \
                          item['tweet_user'] + '/status/' + item['tweet_id'] + ')\n' + item['tweet_time'].strftime(
                        '%Y-%m-%d %H:%M:%S %Z') + '\n\n`' + item[
                              'tweet_text'] + '`'
                    msg = msg.replace('_', r'\_').replace('-', r'\-').replace('#', r'\#')
                    ISHTARider_tg.send_message(-1001982993052, msg
                                               , parse_mode="MarkdownV2", disable_web_page_preview=False)
        # if key:
        msg = [{"role": "assistant",
                "content": "时间:%Y-%m-%d %H:%M:%S %Z,代币token:$token,链chain:#chain,地址address:0x"},
               {"role": "user", "content": tweet_text + "\n根据今天的当前时间today's now:" + time.strftime(
                   '%Y-%m-%d %H:%M:%S %Z %A') + '推测并按照之前回复的格式提取以上内容中代币token(格式为$token)/链chain(格式为#chain)/地址address(格式为0x)/' + '时间(格式为%Y-%m-%d %H:%M:%S %Z)/'.join(
                   key + [''])}]
        print('gpt正在分析文本', key)
        hf = parse('$..hf').find(chat_gpt(msg))[0].value
        print('gpt返回结果', hf)
        item['tweet_ai'] = hf
        # print(len(re.findall(r'unknown', hf, re.I)))
        alpha = re.findall(
            r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+|\$[A-Za-z0-9_]+|#[A-Za-z0-9_]+|0x[A-Za-z0-9_]+',
            hf, re.I)
        tweet_tag = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', str(alpha), re.I)
        item['tweet_tag'] = ' \| '.join(alpha + key)
    # 如果有需要的信息再發送到對應頻道
    if tweet_tag:
        if isinstance(item, CallerItem):
            tg_channel = -1001982993052
            api_url = 'https://alpha-admin.ipfszj.com/api/admin/alpha/caller/add'
            item['alpha_datetime'] = item['tweet_time']
        else:
            tg_channel = -980470620
            api_url = 'https://alpha-admin.ipfszj.com/api/admin/alpha/launch/add'
            try:
                item['alpha_datetime'] = parser.parse(tweet_tag.group())
            except:
                item['alpha_datetime'] = item['tweet_time']
        msg = '[' + item['tweet_user'] + ']' + '(https://twitter\.com/' + item[
            'tweet_user'] + ')' + ' @[' + item[
                  'tweet_alpha'] + ']' + '(https://twitter\.com/' + item[
                  'tweet_alpha'] + ')  \|  [' + item['tweet_tag'] + ']' + '(https://twitter\.com/' + \
              item['tweet_user'] + '/status/' + item['tweet_id'] + ')\n' + item['alpha_datetime'].strftime(
            '%Y-%m-%d %H:%M:%S %Z') + '\n\n`' + item[
                  'tweet_text'] + '`'
        # md解析的特殊字符替換
        msg = msg.replace('_', r'\_').replace('-', r'\-').replace('#', r'\#')
        ISHTARider_tg.send_message(tg_channel, msg
                                   , parse_mode="MarkdownV2", disable_web_page_preview=False)
        item.save()
        item_json = {'tweetId': item['tweet_id'], 'tweetUser': item['tweet_user'],
                     'tweetAlpha': item['tweet_alpha'], 'tweetText': item['tweet_text'],
                     'tweetMedia': item['tweet_media'], 'tweetAi': item['tweet_ai'],
                     'tweetTag': item['tweet_tag'],
                     'alphaDatetime': item['alpha_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                     'userThumb': item['user_thumb'], 'alphaThumb': item['alpha_thumb'],
                     'tweetTime': item['tweet_time'].strftime('%Y-%m-%d %H:%M:%S')}
        token = session.post('https://alpha-admin.ipfszj.com/api/admin/base/open/login',
                             json={'username': 'autoadd', 'password': '123456'}).json().get('data').get('token')
        print('使用管理token', token, session.post(url=api_url, headers={'Authorization': token}, json=item_json))
    print(item.__class__.__name__ + '处理完毕', item, sep='\n')
