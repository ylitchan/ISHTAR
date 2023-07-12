import json
from django.shortcuts import render
from rest_framework.response import Response
from threading import Thread
from rest_framework.decorators import api_view
from django.http import HttpResponse
from ishtarApp.models import *
from utils.tools import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def getbalance(request):
    data = request.data
    user_phone = parse('$..user_phone').find(data)[0].value
    user = UserInfo.objects.get(user_phone=user_phone)
    return Response({'code': 200, 'data': {'user_phone': user_phone, 'user_balance': user.user_balance},
                     'msg': '获取用户余额'})


# 微信小程序验证注册api
@api_view(['POST'])
def signin(request):
    data = request.data
    user_phone = parse('$..user_phone').find(data)[0].value
    password = parse('$..password').find(data)[0].value
    try:
        user = UserInfo.objects.get(user_phone=user_phone, password=password)
        print('当前用户', user)
        return Response({'code': 200, 'data': {'user_phone': user_phone}, 'msg': '登录成功'})
    except:
        return Response({'code': 401, 'data': {'user_phone': user_phone}, 'msg': '账号密码不正确'})


@api_view(['POST'])
def getmsg(request):
    data = request.data
    user_phone = parse('$..user_phone').find(data)[0].value
    try:
        user = UserInfo.objects.get(user_phone=user_phone)
        return Response({'code': 200, 'data': {'user_phone': user_phone, 'user_history': json.loads(user.user_history)},
                         'msg': '获取历史消息'})
    except:
        return Response({'code': 401, 'data': {'user_phone': user_phone}, 'msg': '请重新登录'})


# 微信小程序注册api
@api_view(['POST'])
def register(request):
    data = request.data
    # open_id = parse('$..open_id').find(data)[0].value
    user_phone = parse('$..user_phone').find(data)[0].value
    password = parse('$..password').find(data)[0].value
    try:
        if UserInfo.objects.filter(user_phone=user_phone):
            return Response({'code': 400, 'data': {'open_id': user_phone}, 'msg': '手机号已被注册,请换个手机号'})
        UserInfo.objects.create(open_id=user_phone, user_phone=user_phone, password=password, user_balance=10,
                                user_history=json.dumps([{}]))
        return Response({'code': 200, 'data': {'open_id': user_phone}, 'msg': '注册成功'})
    except:
        return Response({'code': 400, 'data': {'open_id': user_phone}, 'msg': '注册失败'})


# 微信小程序消息api
@api_view(['POST'])
def aichat(request):
    a = time.time()
    data = request.data
    print('客户端消息', data)
    user_phone = parse('$..user_phone').find(data)[0].value
    # 根据open_id查询数据库余额
    user = UserInfo.objects.get(user_phone=user_phone)
    if not user.user_balance:
        return Response({'code': 400, 'data': {'user_phone': user_phone}, 'msg': '余额不足,请联系客服'})
    vx_msg = parse('$..vx_msg').find(data)[0].value
    user_history = json.loads(user.user_history)
    # 1代表gpt
    if parse('$..type').find(data)[0].value:
        hf = chat_gpt(
            [{"role": "assistant", "content": user_history[-1].get('text', '')}, {"role": "user", "content": vx_msg}])
        print('获取到gpt回复', hf)
    else:
        if not user.user_ts:
            ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID, text="<@U053SG7AC01> " + vx_msg, as_user=True)
            # 用消息获取thread_ts，并赋值user['user_ts']
            user.user_ts = get_ts("<@U053SG7AC01> " + vx_msg)
            print('首次消息，发送给claude建立对话获取ts', user.user_ts)
        else:
            ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID, text="<@U053SG7AC01> " + vx_msg, as_user=True,
                                          thread_ts=user.user_ts)
        consumer = producer.pubsub()
        consumer.subscribe(user.user_ts)
        for m in consumer.listen():
            try:
                hf = {'code': 200, 'data': {'hf': m.get('data').decode('utf-8')}, 'msg': 'claude返回结果'}
                print('获取到claude回复', hf)
                break
            except:
                continue
    if hf.get('code', 400) == 200:
        user_history.append({'state': vx_msg, 'text': parse('$..hf').find(hf)[0].value})
        user.user_history = json.dumps(user_history)
        user.user_balance -= 1
        print('扣款成功')
        user.save()
    b = time.time()
    print(b - a, 'ttttttttttttttt')
    return Response(hf)
    # while True:
    #     try:
    #         hf = ts_msg[user['user_ts']].pop()
    #         break
    #     except:
    #         continue
    # print('获取到claude回复', hf)
    # return Response(hf)

    # if not user_thread_ts:
    #     ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID, text="<@U053SG7AC01> " + vx_msg, as_user=True)
    #     print('首次消息，发送给claude建立对话')
    #     # 用消息获取thread_ts，并新建user_ts键值对
    #     user_thread_ts = get_ts("<@U053SG7AC01> " + vx_msg)
    #     user_ts[open_id] = user_thread_ts
    #     print('获取到对应thread_ts，新建user_ts键值对', user_thread_ts,user_ts)
    # while True:
    #     user_thread_ts = get_ts("<@U053SG7AC01> " + vx_msg)
    #     if user_thread_ts:
    #         print('获取到对应thread_ts，新建user_ts键值对',user_ts)
    #         user_ts[open_id] = user_thread_ts
    #         break
    # else:
    #     ISHTAR_slack.chat_postMessage(channel=CHANNEL_ID, text="<@U053SG7AC01> " + vx_msg, as_user=True,thread_ts=user_thread_ts)
    # while True:
    #     try:
    #         hf=ts_msg[user_thread_ts].pop()
    #         break
    #     except:
    #         continue
    # print('获取到claude回复',hf)
    # return Response(hf)


# 这是用于ISHTARider作为slack应用接收处理消息,返回gpt结果
@api_view(['POST'])
def ishtarider(request):
    if "challenge" in request.data:
        # Respond to the Slack challenge
        return Response({"challenge": request.data["challenge"]})
    Thread(target=ISHTARider, args=[request]).start()
    return Response('ISHTARider')


# 这是用于ISHTAR作为slack用户接收处理消息
@api_view(['POST'])
def ishtar(request):
    # 用于slack bot的webhook验证
    if "challenge" in request.data:
        # Respond to the Slack challenge
        return Response({"challenge": request.data["challenge"]})
    Thread(target=ISHTAR, args=[request]).start()
    return Response('ISHTAR')
