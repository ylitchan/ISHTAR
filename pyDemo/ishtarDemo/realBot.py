import speech_recognition as sr
import requests
import json
from gtts import gTTS
# 语音转文字
import slack

# SLACK_TOKEN = "xoxb-5109321480134-5119781200516-a9jKJpORzVF3up5IrAYjU2yb"
SLACK_TOKEN ='xoxp-5109321480134-5118401919620-5164164680115-de663456380ca44774d55961eac9fae1'
CHANNEL_ID = "U053SG7AC01"
client = slack.WebClient(SLACK_TOKEN)
# client.channels_replies(channel=CHANNEL_ID,thread_ts='1682348039.690759',text='asodgn')


response = client.chat_postMessage(
    channel=CHANNEL_ID,
    text="<@U053SG7AC01> 什么时候毁灭人类",as_user=True

)
r = sr.Recognizer()
# with sr.Microphone() as source:
#     print('说点什么吧...')
#     audio = r.listen(source)
# try:
#     text = r.recognize_google(audio, language='zh-CN')
#     print('你说的话是:', text)
# except:
#     print('抱歉,我没有听清楚!')




    # rtm连接和消息读取


# 设置环境变量


# 定义事件处理程序

# 初始化 Slack 客户端


# 初始化 RTM 客户端

# 使用OpenAI的API接口请求GPT-3
# prompt = text + '\nHuman: '
# response = requests.post("https://api.openai.com/v1/engines/davinci/completions",
#     headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
#     json={
#         "prompt": prompt,
#         "max_tokens": 64,
#         "temperature": 0.7,
#         "top_p": 1,
#         "frequency_penalty": 0,
#         "presence_penalty": 0
#     }
# )
# content = json.loads(response.content)
# gpt_response = content['choices'][0]['text']
# # 将生成回复转成语音
# tts = gTTS(gpt_response, lang='zh-CN')
# tts.save('response.mp3')