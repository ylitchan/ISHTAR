import os
import requests
import telebot
response={}
msg_tg = '\=\=新增关注\=\=\n最新关注[' + 'DegenSpartan' + '](https://twitter.com/' + 'DegenSpartan' + ')\nfollowersCount:' + '999' + '\nlistedCount:' + '666' +'\n来自[' + response.get('username','@dao_ust')[
                                                               1:] + '](https://twitter.com/' + response.get(
                        'username','@dao_ust')[1:] + ')'
msg_tg = msg_tg.replace('_', r'\_').replace('-', r'\-').replace('#', r'\#')
ISHTARider_tg = telebot.TeleBot(os.environ.get("ISHTARider_tg"))#.send_message(-1001982993052,'66666666666')
ISHTARider_tg.send_message(-1001982993052, msg_tg, parse_mode="MarkdownV2",
                           disable_web_page_preview=False)


a = requests.get('http://ishtar.freehk.svipss.top/alpha/launching')
print(666666666, a.text)

