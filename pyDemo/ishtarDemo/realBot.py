import speech_recognition as sr
import requests
import json
from gtts import gTTS
# 语音转文字
r = sr.Recognizer()
with sr.Microphone() as source:
    print('说点什么吧...')
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language='zh-CN')
    print('你说的话是:', text)
except:
    print('抱歉,我没有听清楚!')
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