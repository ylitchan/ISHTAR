import openai
import requests
from fastapi import FastAPI,Body
from fastapi.responses import JSONResponse
import uvicorn
import telebot
app = FastAPI()
bot = telebot.TeleBot("6291256191:AAExAaaagpZgEAdBvhOMRN2JxlXr8om4qJA")
openai.api_key = "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"
all={}
async def chatGPT(msg: list):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
        # messages=[
        #     {"role": "user", "content": "未成年人不应该浏览哪些网址，列举20个"},
        # ]
    )
    return u"%s" % res['choices'][0]['message']['content']
@app.post("/")
async def root(json=Body(None)):
    print(json)
    text=json.get('message', {}).get('text','')
    chat_id = json.get('message',{}).get('chat',{}).get('id',0)
    if '/g ' in text:
        user_id = json['message']['from']['id']
        log = all.get(user_id, [])
        log.append({"role": "user", "content": text.replace('/g ', '')})
        hf =await chatGPT(log)
        print(hf)
        msg_id = json['message']['message_id']
        bot.send_message(chat_id, hf, reply_to_message_id=msg_id)
        all[user_id] = [{"role": "user", "content": text.replace('/g ', '')}, {"role": "assistant", "content": hf}]
    elif chat_id == -1001688034062 and text:
        name = json['message']['from'].get('first_name','') + json['message']['from'].get('last_name','')
        reply = '\nreply2:\n' + json['message'].get('reply_to_message',{}).get('text','')
        data = {
            "msgtype": "text",
            "text": {
                "content": name+ ':\n' + text+reply,
            }
        }
        requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=dc326a08-1641-4d78-b5ac-24f143ae7449',
                      json=data)
    return
@app.post("/gpt")
async def gpt(json=Body(None)):
    print(json)
    text=json.get('text','')
    if text:
        hf = await chatGPT([{"role": "user", "content": text}])
        return JSONResponse(content=hf)
    return


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8080)
