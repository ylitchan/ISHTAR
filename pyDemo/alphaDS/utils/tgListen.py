from pyrogram import Client
from tools import *

proxy = {
    "scheme": "http",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",
    "port": 10810,
    # "username": "username",
    # "password": "password"
}
app = Client("my_account", os.getenv('api_id'), os.getenv('api_hash'), proxy=proxy)


@app.on_message()
async def raw(client, message):
    name = ''
    if hasattr(message, 'from_user') and message.from_user:
        user_id = str(message.from_user.id)
        for i in [message.from_user.first_name, message.from_user.last_name]:
            if i:
                name += i
    else:
        user_id = '-1623440846'
    if hasattr(message, 'chat'):
        try:
            chat_username = message.chat.username
        except:
            chat_username = 'UST_DAO'
    elif hasattr(message, 'sender_chat'):
        try:
            chat_username = message.sender_chat.username
        except:
            chat_username = 'UST_DAO'
    else:
        chat_username = 'UST_DAO'
    if message.chat.title == '涩谷俱乐部':
        print(message.chat.title, message.text, message.date.strftime("%Y-%m-%d %H:%M:%S %Z %A"), message.id, name,
              chat_username, user_id, sep='\n')
        if message.text:
            q_alpha.put('tg',
                        [message.chat.title, message.text, message.date.strftime("%Y-%m-%d %H:%M:%S %Z %A"), message.id,
                         name,
                         chat_username, user_id])


if __name__ == '__main__':
    app.run()
