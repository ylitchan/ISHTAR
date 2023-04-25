import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token='xoxb-5109321480134-5176972648513-f4PC9uQWKgNDUS7t8JMBabOm')

@app.message(":wave:")
def say_hello(message):
    print(66666)
    user = message['user']

if __name__ == "__main__":
    SocketModeHandler(app, 'xapp-1-A054WLW9HNG-5161522001573-676b5dd7a4d9550d95ccb36809484e84f160cf32d86289f07a0d7592d5a420c7').start()

