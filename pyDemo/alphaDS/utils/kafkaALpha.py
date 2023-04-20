import datetime
import random
import time
import requests
from tools import *
def add_member(userId):
    headers = {
        'cookie': 'des_opt_in=Y; _gcl_au=1.1.116267149.1676257589; g_state={"i_l":4,"i_p":1681369247236}; _ga_BYKEBDM7DS=GS1.1.1679899771.1.1.1679899844.0.0.0; _gid=GA1.2.1222660834.1680783998; at_check=true; mbox=PC#5d50de66cc054e10bf959bf00d0b670c.38_0#1744731433|session#db24585874f049b1b132445cb93bebc8#1681488493; _ga=GA1.2.1915858432.1679573193; kdt=2RNumTWyrbgn13h0nBHx95uYSPlUa6qMK390ud8K; _ga_34PHSZMC42=GS1.1.1681533194.15.0.1681533194.0.0.0; dnt=1; auth_multi="1568898000654680064:17e8044520b62a806dc73e68c70a019d1918e70f"; auth_token=614cb847793f6b268a64e8cf6ea05479d38bb67d; guest_id_ads=v1:168153922613435906; guest_id_marketing=v1:168153922613435906; lang=en; guest_id=v1:168153922613435906; twid=u=1573326306661793792; ct0=5bb87294748eabc856cd95ffc52dad00c7ef7abe56a299feebef81091739e80961b2842233a9a2222093250ad0270f0aedcb49afaeded4e26fa13092ad22b2cda67ba9a6ddc4ef96c139e351f9cbcaaa; personalization_id="v1_A5Cjem2NxpnAPzInu7PDFA=="',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
        'x-csrf-token': '5bb87294748eabc856cd95ffc52dad00c7ef7abe56a299feebef81091739e80961b2842233a9a2222093250ad0270f0aedcb49afaeded4e26fa13092ad22b2cda67ba9a6ddc4ef96c139e351f9cbcaaa'
        }
    var = {
        "variables": {
            "listId": "1639838455760035840",
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
    headers = {
        'cookie': 'des_opt_in=Y; _gcl_au=1.1.116267149.1676257589; g_state={"i_l":4,"i_p":1681369247236}; _ga_BYKEBDM7DS=GS1.1.1679899771.1.1.1679899844.0.0.0; mbox=PC#5d50de66cc054e10bf959bf00d0b670c.38_0#1744731433|session#db24585874f049b1b132445cb93bebc8#1681488493; _ga=GA1.2.1915858432.1679573193; _ga_34PHSZMC42=GS1.1.1681533194.15.0.1681533194.0.0.0; kdt=h36Lkx200pHHLSt2tM4Yz2JChWa3VX3gcj2Ywy4e; _gid=GA1.2.1864480522.1681736613; dnt=1; ads_prefs="HBESAAA="; auth_multi="1573326306661793792:612997b9f97500591e7d9ed2eb503c6a2b2f4d13"; auth_token=6a428ef19a32c348954ac2200680be380092af01; lang=zh-cn; guest_id=v1:168208164180005742; twid=u=1568898000654680064; ct0=328479905feeceae17422587781506a543bf77854dc0971628d182aa8baa4f598f1223f46bde86349c26bb53e62bff9058b2595e0932fc763f7e762d2d4380c94c83f2e7d2b2ec8cc9fbe79e88ae7a45; guest_id_marketing=v1:168208164180005742; guest_id_ads=v1:168208164180005742; personalization_id="v1_TDhwQ0RRjy5ZhLK5q8YMeA=="',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
        'x-csrf-token': '328479905feeceae17422587781506a543bf77854dc0971628d182aa8baa4f598f1223f46bde86349c26bb53e62bff9058b2595e0932fc763f7e762d2d4380c94c83f2e7d2b2ec8cc9fbe79e88ae7a45'
    }
    res = requests.post('https://twitter.com/i/api/graphql/x0smnIS1jLLXToRYg70g4Q/ListAddMember', headers=headers,json=var)
    print('推特列表添加',res)

# 创建消费者实例
consumer = KafkaConsumer('alpha', bootstrap_servers=['localhost:9092'], group_id='alpha-group')
# 消费消息
for message in consumer:
    print('当前kafka消费时间',message.value.decode('utf-8'),datetime.datetime.now())
    add_member(message.value.decode('utf-8'))
    time.sleep(random.uniform(432, 576))


