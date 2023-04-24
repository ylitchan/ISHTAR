import re
import moviepy.editor as mpe
import requests
import speech_recognition as sr
from tools import *
from django.shortcuts import render
from jsonpath_ng import parse
import slack
# Create your views here.
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def newproject(request):
    lookup_fields = request.data.get('lookup_fields', '')
    order_fields = request.data.get('order_fields', '')

    # 校验lookup_fields和order_fields
    if lookup_fields:
        pass
    if order_fields:
        pass

    return Response(
        {"username": "@ust_dao", "FollowedToday": 1, "Followers": 1, "Bio": "UST DAO 牛逼", "Created": "04/22/2023",
         "DiscoveryTime": "2023-04-22"})


@api_view(['POST'])
def launching(request):
    lookup_fields = request.data.get('lookup_fields', '')
    order_fields = request.data.get('order_fields', '')

    # 校验lookup_fields和order_fields
    if lookup_fields:
        pass
    if order_fields:
        pass

    return Response({"tweet_user": "ust_dao", "tweet_alpha": " @dao_ust", "tweet_text": "UST DAO 牛逼plus",
                     "user_thumb": "https://api.cyfan.top/acg",
                     "tweet_media": "https://pbs.twimg.com/media/FuKsFCUaMAAK0wy.jpg", "alpha_time": "2023-04-23",
                     "tweet_time": "2023-04-22"})


@api_view(['POST'])
def ishtar(request):
    print(request.data)
    file_id = parse('$..file_id').find(request.data)[0].value
    ISHTAR = telebot.TeleBot('6074723596:AAEeU2OjyTYVwf0fsLN854qe6X92prsEli8')
    file_url = ISHTAR.get_file_url(file_id)
    response = requests.get(file_url)

    with open('input.oga', 'wb') as f:
        f.write(response.content)
    audioclip = mpe.AudioFileClip("input.oga")
    audioclip.write_audiofile("output.wav")
    r = sr.Recognizer()
    with sr.AudioFile('output.wav') as source:
        # 将语音文件读取为AudioData对象
        audio_data = r.record(source)
    # 使用Google Speech Recognition进行识别
    text = r.recognize_google(audio_data, language='zh-CN')

    # 输出识别结果
    print(text)

    # SLACK_TOKEN = "xoxb-5109321480134-5119781200516-a9jKJpORzVF3up5IrAYjU2yb"
    SLACK_TOKEN = 'xoxp-5109321480134-5118401919620-5153089528371-48fc79253ec7046c7a4263436e3b43f5'
    CHANNEL_ID = "D053AUX5GDB"#"C052ZB95CQP"

    client = slack.WebClient(SLACK_TOKEN)
    response = client.chat_postMessage(
        channel=CHANNEL_ID,
        text="<@U053SG7AC01> " + text, as_user=True

    )

    return Response('ISHTAR')
