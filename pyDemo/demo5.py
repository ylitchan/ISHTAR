import os
from slack_sdk import

# 设置环境变量
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

# 定义事件处理程序
@RTMClient.run_on(event="message")
def handle_message(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    if "text" in data:
        text = data["text"]
        print(text)

# 初始化 RTM 客户端
rtm_client = RTMClient(token=SLACK_BOT_TOKEN)

# 运行客户端
rtm_client.start()
