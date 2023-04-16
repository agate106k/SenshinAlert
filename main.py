import os
import time
import requests
import json
from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, PostbackEvent
from message_func import message_func
from udp_client_multithread_plot import sensor_check

app = Flask(__name__) 
channel_secret = "1847cd7edb82c8b54ede7e809608da5f"
channel_access_token = "z4fIHlabijfWmFHiTXEpWYp+zqYZITdfokeZlRxzIvwABdifuvsAEmRRuERU4bYs7hBB+qHpNhKppLDAMzawNf6RBTK5OwPI1kSeh7b4pF/TaXqkWmw7FLTl/FUSSqkJ1YWj1binaFqq7444Y2ow2wdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
gaswebhook = "https://script.google.com/macros/s/AKfycbxa19Awjede9LYuqPNrqktm45NR43V0WlJy3arDSNnD6or_yIFZn6r-fPFM2sAIq3MW/exec"
webhookinspector = "https://webhook.site/35bfdf84-300d-41bc-bc43-7da338ee2c1c"


# LINE DevelopersのWebhookに指定したURLにリクエストを送信して、問題がなければhandleに定義されている関数を呼ぶ
@app.route("/callback", methods=['POST'])

def callback(): 
    body = request.get_data(as_text=True)        
    app.logger.info("Request body: " + body)     
    body = request.get_data(as_text=True)
    data = json.loads(body)

    # イベントオブジェクトを取得する
    event = data["events"][0]
    print(event)
    headers = {
        'Content-Type': 'application/json',
    }
    requests.post(gaswebhook, headers=headers, data=request.get_data())
    requests.post(webhookinspector, headers=headers, data=request.get_data())
    
    message_func(event)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    headers = {
        'Content-Type': 'application/json',
    }
    # res = requests.post(gaswebhook, headers=headers, data=request.get_data())
    # print(res)
    print("comeon")
    message_func(event)
 
if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port ] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8080, help='port')#8000だとできなかった
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()
    app.run(debug=options.debug, port=options.port)
    