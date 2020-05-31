from flask import Flask , request,abort
from linebot import(
    LineBotApi , WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent , TextMessage , TextSendMessage , ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi("78A2zLim1iS0CaUX8VDViSXzPmz2DKN6/eAdapVFXMpFXwtVRjF1K31uLeiVIQU4suIt0irP/yxLcCgbvtEOkzWXuE6IxrglZCLoA0v+YrjdLdnUuRHe9pCEz1/GFZn1K6N2lNUxt+TL+HtSJJfosQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("931dcb19cd7ec1ffe867222b36840598")

@app.route("/callback" , methods=["POST"])
def callback():
  # sign
  signature = request.headers["X-Line-Signature"]
  
  body = request.get_data(as_text=True)
  app.logger.info("Request body:" + body)
  try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
  
@handler.add(MessageEvent , message= TextMessage)
def handle_message(event):
  line_bot_api.reply_message(
      event.reply_token,
      TextSendMessage(text=event.message.text))