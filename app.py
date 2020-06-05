from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__, static_url_path='')

# Channel Access Token
line_bot_api = LineBotApi('Fg9jPHw4MFplDYS+trdjxGSy5ocKjphlFYubeu3l2g89GX4+Ffn0tAESnevUbL+QsuIt0irP/yxLcCgbvtEOkzWXuE6IxrglZCLoA0v+YriUdrOKAmBTYCnKx4iIZYyhrAAD39jp7eqLsnVKumj7vQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('931dcb19cd7ec1ffe867222b36840598')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = "https://docs.google.com/forms/d/1BPtFuQSFuUEIfqDut-iJJBk2k8whN4JmRidmz_Oabjo/edit?usp=drivesdk"
    user_id = event.source.user_id
    msg += "\n" + user_id 
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))


#import os
if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 4040))
    #app.run(host='127.0.0.1', port=port)
    app.run()
