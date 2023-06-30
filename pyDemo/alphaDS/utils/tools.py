import json
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
from threading import Thread
from pybloom_live import ScalableBloomFilter
import random
import speech_recognition as sr
import redis
from pygtrans import Translate
from alphaPlan.items import *

# 消息生产者
# q_add = queue.Queue()
# q_alpha = queue.Queue()
client_translate = Translate()
producer = redis.Redis(host='localhost', port=6379)
appid = os.getenv('AppID')
secret = os.getenv('AppSecret')
ISHTARider_tg = telebot.TeleBot(os.environ.get("ISHTARider_tg"))
ISHTAR_slack = WebClient(os.getenv('ISHTAR_slack'))
ISHTARider_slack = WebClient(os.getenv('ISHTARider_slack'))
openai.api_key = os.environ.get('openai')
bot = telebot.TeleBot(os.environ.get("telebot"))
client_tweet = tweepy.Client(
    bearer_token=os.environ.get("bearer_token"),
    consumer_key=os.environ.get("consumer_key"),
    consumer_secret=os.environ.get("consumer_secret"),
    access_token=os.environ.get("access_token"),
    access_token_secret=os.environ.get("access_token_secret"))

# client_tweet=tweepy.Client(access_token='Yy1VQnhiOF85ekRCWDkycC1QTG06MTpjaQ',access_token_secret='786mRbuWeqVvnodLNStsfd1KlhgVtM5mcUm85UnIUQ70c')


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


def add_member():
    account_list = [('dao_ust', '1639838455760035840', {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; kdt=YY5epcm5ePgzHpX3oXabVshhh27g18lEHMuYH7v4; _gid=GA1.2.1842052750.1687350267; dnt=1; auth_multi="1577862800952930305:1bedb7ef5487e0ca4faa75e233f94abf2b7e59eb|1573326306661793792:b8da11bc85168214fe4b0b6957cc318478a3a6e2"; auth_token=5503c671b8069c470766fdea2d66ba5fb9a86538; guest_id=v1%3A168735332699056847; ct0=e19897d7753735caf08114c7dddf607957a28df444b776c21a2b74b16100bd05790d7cdf5b6c32478aa17ed0eb87520b121e6c39235f656d71973706e3c270b64f7c888caee8ebd78b5d003f9ab97ae8; lang=zh-cn; twid=u%3D1568898000654680064; guest_id_marketing=v1%3A168735332699056847; guest_id_ads=v1%3A168735332699056847; personalization_id="v1_quUYBDnAEMLTiqebrNCQJQ=="',
        'X-Csrf-Token': 'e19897d7753735caf08114c7dddf607957a28df444b776c21a2b74b16100bd05790d7cdf5b6c32478aa17ed0eb87520b121e6c39235f656d71973706e3c270b64f7c888caee8ebd78b5d003f9ab97ae8'}),
                    ('dao_ust2', '1667054883219083264', {
                        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                        'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; _gid=GA1.2.294164188.1687613031; gt=1672929356564557831; kdt=NM3A3BOWMx37GmPm0Z4Lhye1iVVcztVSlceYK2X6; lang=zh-cn; dnt=1; auth_multi="1121014957422907392:fb739a04e9f024dfa6860b837b9c437aaa93f0fa"; auth_token=450444b721eb21cfa581e4195ac7384545dd89cc; guest_id=v1%3A168769252221011498; ct0=1a3a1a3f3f3497d56d958b4363e1514dbfd5f90dd3cec4455a20d0223c656bfd9786b307c96508e2f85501c6c137ae9dab5cddf5f6b3655c6d3b11f72d39041376df5f2b01920c2b148c3389e8fc1bca; twid=u%3D1666748651618865153; guest_id_marketing=v1%3A168769252221011498; guest_id_ads=v1%3A168769252221011498; personalization_id="v1_BLq9lVhxG6JsQL5ss6yM5g=="',
                        'X-Csrf-Token': '1a3a1a3f3f3497d56d958b4363e1514dbfd5f90dd3cec4455a20d0223c656bfd9786b307c96508e2f85501c6c137ae9dab5cddf5f6b3655c6d3b11f72d39041376df5f2b01920c2b148c3389e8fc1bca'}),
                    ('dao_ust3', '1646838020363153408', {
                        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                        'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; kdt=YY5epcm5ePgzHpX3oXabVshhh27g18lEHMuYH7v4; _gid=GA1.2.1842052750.1687350267; dnt=1; lang=zh-cn; auth_multi="1568898000654680064:5503c671b8069c470766fdea2d66ba5fb9a86538|1577862800952930305:1bedb7ef5487e0ca4faa75e233f94abf2b7e59eb|1573326306661793792:b8da11bc85168214fe4b0b6957cc318478a3a6e2"; auth_token=bc4e0b0e13059d5f73217d2e512963ab84d2b03c; guest_id=v1%3A168735792361821059; ct0=5f9cd12434705cc3270ebe333b8b3cfa6f4df1fbd15306751b4c853d4cfb650082da2b70ebecb3d60552549c151c4fa4d17a8ef20969692024ec5aeabc572bfc2e7a2634167d48c2347572bf87a20c54; twid=u%3D1121014957422907392; guest_id_marketing=v1%3A168735792361821059; guest_id_ads=v1%3A168735792361821059; personalization_id="v1_dhsI3gVYY2Bo9x07dcPgzg=="',
                        'X-Csrf-Token': '5f9cd12434705cc3270ebe333b8b3cfa6f4df1fbd15306751b4c853d4cfb650082da2b70ebecb3d60552549c151c4fa4d17a8ef20969692024ec5aeabc572bfc2e7a2634167d48c2347572bf87a20c54'})]
    with open('sbfilterMember', 'rb') as f:
        sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH).fromfile(f)
    consumer = producer.pubsub()
    consumer.subscribe('q_add')
    # 初始化布隆过滤器
    # sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
    # with open('listMembers.json', 'r') as f:
    #     list_members = json.load(f)
    # for member in list_members:
    #     sbfilter.add(member)
    start_time = time.time()
    number = 0
    index = 0
    # member = client_tweet.get_list_members('1667547733119627265', pagination_token=None, user_auth=True)
    # next_token = member.meta.get('next_token')
    # already = {i.id for i in member.data}
    # print('列表数量', len(already))
    # while next_token:
    #     try:
    #         member = client_tweet.get_list_members('1667547733119627265', pagination_token=next_token)
    #         next_token = member.meta.get('next_token')
    #         already.update([i.id for i in member.data])
    #         time.sleep(60)
    #     except:
    #         time.sleep(900)
    #         continue
    for m in consumer.listen():
        new_follow = m.get('data')
        if isinstance(new_follow, int):
            continue
        new_follow = json.loads(new_follow)
        new_follow_id = new_follow.get('restID', 0)
        # while True:
        #     new_follow = q_add.get(block=True)
        # try:
        #     # new_follow_id = client_tweet.get_user(username=new_follow,
        #     #                                       user_fields=["profile_image_url", "public_metrics",
        #     #                                                    'created_at',
        #     #                                                    'description']).data
        #
        #     new_user = session.get(
        #         'https://twitter.com/i/api/graphql/qRednkZG-rn1P6b48NINmQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22{}%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D'.format(
        #             new_follow), headers=account_list[index][2]).json()
        #     new_follow_id = int(parse('$..rest_id').find(new_user)[0].value)
        # except:
        #     producer.publish('q_add', new_follow)
        #     time.sleep(300)
        #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '获取错误', account_list[index][0], new_follow)
        #     continue
        #     # Thread(target=add_member, args=[q_add], daemon=False).start()
        #     # break
        #     # 發送添加到列表的請求
        if not sbfilter.add(new_follow_id):
            index += 1
            if index == 3:
                index = 0
            # print('添加关注', new_follow.username)
            delta_time = time.time() - start_time
            try:
                # 每请求一次计数加1
                # added = client_tweet.add_list_member(id='1639838455760035840', user_id=new_user.id, user_auth=True)
                added = session.post('https://twitter.com/i/api/graphql/27lfFOrDygiZs382QLttKA/ListAddMember',
                                     headers=account_list[index][2],
                                     json={
                                         "variables": {
                                             "listId": account_list[index][1],
                                             "userId": new_follow_id
                                         },
                                         "features": {
                                             "rweb_lists_timeline_redesign_enabled": True,
                                             "responsive_web_graphql_exclude_directive_enabled": True,
                                             "verified_phone_label_enabled": False,
                                             "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                                             "responsive_web_graphql_timeline_navigation_enabled": True
                                         },
                                         "queryId": "27lfFOrDygiZs382QLttKA"
                                     }).json()
                number += 1
                token = session.post('https://alpha-admin.ipfszj.com/api/admin/base/open/login',
                                     json={'username': 'autoadd', 'password': '123456'}).json().get(
                    'data').get(
                    'token')
                new_follow.update({'listId': parse('$..id_str').find(added)[0].value,
                                   'listName': parse('$..name').find(added)[0].value,
                                   'listAccount': parse('$..screen_name').find(added)[0].value})
                session.post(url='https://alpha-admin.ipfszj.com/api/admin/alpha/list/add',
                             headers={'Authorization': token},
                             json=new_follow)
                print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加成功', account_list[index][0], new_follow)
                # if added.data.get('is_member'):
                #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加成功', new_user.username)
                #     list_members.append(new_user.id)
                # else:
                #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加失败', new_user.username)
                #     q_add.put(new_follow)
            except:
                time.sleep(300)
                print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加错误', account_list[index][0], new_follow)
                # 在15分钟内添加4次就暂停到满15分钟
            if number == 4 and delta_time < 900:
                with open('sbfilterMember', 'wb') as f:
                    sbfilter.tofile(f)
                print('超过频率,等待')
                time.sleep(930 - delta_time)
                start_time = time.time()
                number = 0
            elif delta_time >= 900:
                with open('sbfilterMember', 'wb') as f:
                    sbfilter.tofile(f)
                print('重置为1')
                start_time = time.time()
                number = 1

            # except:
            #     producer.publish('q_add', new_follow)
            #     time.sleep(300)
            #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加错误', account_list[index][0], new_follow)
            #     continue
            # Thread(target=add_member, args=[q_add], daemon=False).start()
            # break
        #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加错误', new_follow.username)
        #     time.sleep(900)
        #         Thread(target=add_member, args=[q_add], daemon=False).start()
        #     break
        # # 获取最后一页,将其加进already
        # member = client_tweet.get_list_members('1639838455760035840', pagination_token=final_token)
        # next_token = member.meta.get('next_token')
        # if next_token:
        #     final_token = next_token
        #     already.update([i.id for i in client_tweet.get_list_members('1639838455760035840',
        #                                                                 pagination_token=final_token).data])
        # else:
        #     already.update([i.id for i in member.data])
        # # 添加失败重新放入队列
        # if new_follow.id not in already:
        #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加失败,重新放入队列')
        #     q_add.put(new_follow.id)
        #     # producer.publish('tg_add', user_id)
        #     time.sleep(3600)
        # else:
        #     print(time.strftime('%Y-%m-%d %H:%M:%S %Z %A'), '添加成功,计入已添加')
        #     already.update(new_follow.id)
        #     time.sleep(10)


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
# def get_openid(data):
#     code = parse('$..code').find(data)[0].value
#     res = session.get(
#         'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
#             appid, secret, code))
#     return parse('$..openid').find(res.json())[0].value


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
        # print(thread_ts[0].value)
        channel = parse('$..channel').find(data)[0].value
        bot_id = parse('$..bot_id').find(data)
        # 判斷是否首個消息沒有ts
        if channel == 'C052ZB95CQP' and not thread_ts:
            ts = parse('$..ts').find(data)[0].value
            producer.publish(text, ts)
            # new_ts[ts] = text
            # ts_msg[ts] = []
            print('首条消息,新建thread_ts')
        # 將claude的消息發到對應的redis頻道
        elif channel == 'C052ZB95CQP' and bot_id[0].value == 'B0543J2N27J':
            producer.publish(thread_ts[0].value, text)
            # ts_msg[thread_ts[0].value].insert(0, text)
            print('添加新消息到thread_ts')
        # 喊单处理的频道
        elif channel == 'C05B6HT06R0' and bot_id[0].value == 'B0543J2N27J':
            tweet_id = re.search('@\d+', text).group().replace('@', '')
            producer.publish(tweet_id, text)
            print('添加新消息到', tweet_id)
        # 发射时间的频道
        elif channel == 'C05B3HVQ8J1' and bot_id[0].value == 'B0543J2N27J':
            tweet_id = re.search('@\d+', text).group()
            producer.publish(tweet_id, text)
            print('添加新消息到', tweet_id)


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
    # 优先使用gpt进行分析,list类型的key为LaunchItem
    if not isinstance(key, list) and not item['tweet_text'].startswith('RT @'):
        msg = [{"role": "assistant", "content": "我现在是一名分析师,{乐观态度:$token}"},
               {"role": "user",
                "content": tweet_text + '\n按照之前回复的格式提取以上内容中作者持乐观态度的代币。若无对应项则该项放空'}]
        print('gpt正在分析文本', key.group())
    elif isinstance(key, list):
        # 有dc鏈接就發送
        if item['tweet_alpha'] == 'discord':
            # 把鏈接從key中拿掉,避免影響後面的launch判斷
            for i in key:
                if 'https://t.co/' in i:
                    key.remove(i)
                    msg_tg = '[' + item['tweet_user'] + ']' + '(https://twitter\.com/' + item[
                        'tweet_user'] + ')' + ' @[' + item[
                                 'tweet_alpha'] + ']' + '(https://twitter\.com/' + item[
                                 'tweet_alpha'] + ')  \|  [discord]' + '(https://twitter\.com/' + \
                             item['tweet_user'] + '/status/' + item['tweet_id'] + ')\n' + item['tweet_time'].strftime(
                        '%Y-%m-%d %H:%M:%S %Z') + '\n\n`' + client_translate.translate(
                        item['tweet_text']).translatedText + '`'
                    msg_tg = msg_tg.replace('_', r'\_').replace('-', r'\-').replace('#', r'\#')
                    ISHTARider_tg.send_message(-1001982993052, msg_tg
                                               , parse_mode="MarkdownV2", disable_web_page_preview=False)
        msg = [{"role": "assistant",
                "content": "我现在是一名分析师,{代币时间:%Y-%m-%d %H:%M:%S %Z,代币token:$token,链chain:#chain,' \
                                             '合约address:0x}"},
               {"role": "user",
                "content": tweet_text + "\n我告诉你现在的时间是:" + time.strftime(
                    '%Y-%m-%d %H:%M:%S %Z %A') + '推测并按照之前回复的格式提取以上内容中代币token(格式为$token)/链chain(格式为#chain)/合约address('
                                                 '格式为0x)/' + '时间(格式为%Y-%m-%d %H:%M:%S %Z)/'.join(
                    ['代币' + k for k in key] + ['']) + '。若无对应项则该项放空'}]
        print('gpt正在分析文本', key)
    else:
        return
    hf = parse('$..hf').find(chat_gpt(msg))[0].value
    if 'gpt error' not in hf:
        print('gpt返回结果', hf)
    # 如果gpt故障,使用claude分析,不同类型的item使用不同频道
    else:
        print('gpt返回错误', hf)
        return
        if isinstance(item, CallerItem) and not item['tweet_text'].startswith('RT @'):
            channel_slack = 'C05B6HT06R0'
            text_slack = '推文id@' + item[
                'tweet_id'] + ':\n' + tweet_text + '\n按照{推文id:@id,乐观态度:$token}的格式提取以上内容中推文id(格式为@id)/作者持乐观态度的代币(' \
                                                   '格式为$token)。若无对应项则该项放空'
            sub = '@' + item['tweet_id']
            print('claude正在分析文本', key.group())
        elif isinstance(item, LaunchItem):
            channel_slack = 'C05B3HVQ8J1'
            text_slack = '推文id@' + item[
                'tweet_id'] + ':\n' + tweet_text + "\n我告诉你现在的时间是:" + time.strftime(
                '%Y-%m-%d %H:%M:%S %Z %A') + '推测并按照{推文id:@id,代币时间:%Y-%m-%d %H:%M:%S %Z,代币token:$token,链chain:#chain,' \
                                             '合约address:0x}的格式提取以上内容中推文id(格式为@id)/代币token(格式为$token)/链chain(' \
                                             '格式为#chain)/合约address(格式为0x)/' + '时间(格式为%Y-%m-%d %H:%M:%S %Z)/'.join(
                ['代币' + k for k in key] + ['']) + '。若无对应项则该项放空'
            sub = item['tweet_id']
            print('claude正在分析文本', key)
        else:
            return
        ISHTAR_slack.chat_postMessage(channel=channel_slack, text="<@U053SG7AC01> " + text_slack, as_user=True)
        consumer = producer.pubsub()
        consumer.subscribe(sub)
        for m in consumer.listen():
            hf = m.get('data')
            if isinstance(hf, int):
                continue
            hf = hf.decode('utf-8')
            break
        print('claude返回结果', hf)
    item['tweet_ai'] = hf
    # 根據不同的類型用不同的参数和方法
    if isinstance(item, CallerItem):
        tweet_tag = set(re.findall('\$[A-Za-z]+', hf, re.I))
        tweet_tag = ' \| '.join(tweet_tag).replace('$token', '')
        item['tweet_tag'] = tweet_tag
        tg_channel = -1001982993052
        api_url = 'https://alpha-admin.ipfszj.com/api/admin/alpha/caller/add'
        item['alpha_datetime'] = item['tweet_time']
    else:
        alpha = re.findall(
            r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+|\d{4}-\d{2}-\d{2}|\$[A-Za-z0-9_]+|#[A-Za-z0-9_]+|0x[A-Za-z0-9_]+',
            hf, re.I)
        tweet_tag = re.search(r'\d{4}-\d{2}-\d{2}', str(alpha), re.I)
        item['tweet_tag'] = ' \| '.join(set(alpha + key))
        tg_channel = -980470620
        api_url = 'https://alpha-admin.ipfszj.com/api/admin/alpha/launch/add'
        try:
            item['alpha_datetime'] = parser.parse(tweet_tag.group())
        except:
            item['alpha_datetime'] = item['tweet_time']
    # 如果有需要的信息再發送到對應頻道
    if tweet_tag:
        msg_tg = '[' + item['tweet_user'] + ']' + '(https://twitter\.com/' + item[
            'tweet_user'] + ')' + ' @[' + item[
                     'tweet_alpha'] + ']' + '(https://twitter\.com/' + item[
                     'tweet_alpha'] + ')  \|  [' + item['tweet_tag'] + ']' + '(https://twitter\.com/' + \
                 item['tweet_user'] + '/status/' + item['tweet_id'] + ')\n' + item['alpha_datetime'].strftime(
            '%Y-%m-%d %H:%M:%S %Z') + '\n\n`' + item['tweet_text'] + '`'
        # md解析的特殊字符替換
        msg_tg = msg_tg.replace('_', r'\_').replace('-', r'\-').replace('#', r'\#')
        ISHTARider_tg.send_message(tg_channel, msg_tg
                                   , parse_mode="MarkdownV2", disable_web_page_preview=False)
        item.save()
        item_json = {'tweetId': item['tweet_id'], 'tweetUser': item['tweet_user'],
                     'tweetAlpha': item['tweet_alpha'], 'tweetText': item['tweet_text'],
                     'tweetMedia': item['tweet_media'], 'tweetAi': item['tweet_ai'],
                     'tweetTag': item['tweet_tag'], 'listAccount': item['list_account'],
                     'alphaDatetime': item['alpha_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                     'userThumb': item['user_thumb'], 'alphaThumb': item['alpha_thumb'],
                     'tweetTime': item['tweet_time'].strftime('%Y-%m-%d %H:%M:%S')}
        token = session.post('https://alpha-admin.ipfszj.com/api/admin/base/open/login',
                             json={'username': 'autoadd', 'password': '123456'}).json().get('data').get('token')
        print('使用管理token', token, session.post(url=api_url, headers={'Authorization': token}, json=item_json))
    print(item.__class__.__name__ + '处理完毕', item, sep='\n')
