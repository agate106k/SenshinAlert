import os
import requests
import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage
from udp_client_multithread_plot import sensor_check
channel_access_token = "z4fIHlabijfWmFHiTXEpWYp+zqYZITdfokeZlRxzIvwABdifuvsAEmRRuERU4bYs7hBB+qHpNhKppLDAMzawNf6RBTK5OwPI1kSeh7b4pF/TaXqkWmw7FLTl/FUSSqkJ1YWj1binaFqq7444Y2ow2wdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(channel_access_token)
gaswebhook = "https://script.google.com/macros/s/AKfycbxa19Awjede9LYuqPNrqktm45NR43V0WlJy3arDSNnD6or_yIFZn6r-fPFM2sAIq3MW/exec"
webhookinspector = "https://webhook.site/35bfdf84-300d-41bc-bc43-7da338ee2c1c"
# 0 sleep 1 wake up  2 wake up but lying with smartphone 3 wake up just using smart phone 99 switch off
# def test():
#     channel_access_token = channel_access_token = "z4fIHlabijfWmFHiTXEpWYp+zqYZITdfokeZlRxzIvwABdifuvsAEmRRuERU4bYs7hBB+qHpNhKppLDAMzawNf6RBTK5OwPI1kSeh7b4pF/TaXqkWmw7FLTl/FUSSqkJ1YWj1binaFqq7444Y2ow2wdB04t89/1O/w1cDnyilFU="
#     user_id = 'U76b3758a48ee8ef891ab61171aa5d7a7'

#     # LineBotApiオブジェクトを作成
#     line_bot_api = LineBotApi(channel_access_token)
#     # status textを作成
#     # status = sensor_check()
#     status_text = "sleep"
#     line_bot_api.push_message(user_id, TextSendMessage(text=status_text))
#     headers = {
#         'Content-Type': 'application/json',
#     }
#     data = {

#         "events": [
#             {
#             "type": "message",
#             "message": {
#                 "type": "text",
#                 "text": "sleep"
#             },
#             "source": {
#                 "type": "user",
#                 "userId": "U76b3758a48ee8ef891ab61171aa5d7a7"
#             },
#             "mode": "active"
#             }
#         ]
#         }

#     # POSTリクエストを送信する
#     # response = requests.post(gaswebhook, json=data)
#     requests.post(gaswebhook, headers=headers, json=data)
#     requests.post(webhookinspector, headers=headers, json=data)
def get_status_text(status):
    if status == 0:
        return "Kei is Sleeping"
    elif status == 1:
        return "Kei already wake up"
    elif status == 2:
        return "Kei already wake up but lying with using smartphone"
    elif status == 3:
        return "Just using smart phone"
    elif status == 99:
        return "switch off"
    else:
        return "unknown status"
def message_func(event):
    print("get")
    if event["type"] == "message":
        messe = event["message"]["text"]
        
        if messe == "check":
            # 判定をここに入れる。
            channel_access_token = channel_access_token = "z4fIHlabijfWmFHiTXEpWYp+zqYZITdfokeZlRxzIvwABdifuvsAEmRRuERU4bYs7hBB+qHpNhKppLDAMzawNf6RBTK5OwPI1kSeh7b4pF/TaXqkWmw7FLTl/FUSSqkJ1YWj1binaFqq7444Y2ow2wdB04t89/1O/w1cDnyilFU="
            user_id = 'U76b3758a48ee8ef891ab61171aa5d7a7'

            # LineBotApiオブジェクトを作成
            line_bot_api = LineBotApi(channel_access_token)
            # status textを作成
            status = sensor_check()
            status_text = get_status_text(status)
            line_bot_api.push_message(user_id, TextSendMessage(text=status_text))
            headers = {
                'Content-Type': 'application/json',
            }
            data = {

                "events": [
                    {
                    "type": "message",
                    "message": {
                        "type": "text",
                        "text": status_text
                    },
                    "source": {
                        "type": "user",
                        "userId": "U76b3758a48ee8ef891ab61171aa5d7a7"
                    },
                    "mode": "active"
                    }
                ]
                }

            # POSTリクエストを送信する
            # response = requests.post(gaswebhook, json=data)
            requests.post(gaswebhook, headers=headers, json=data)
            requests.post(webhookinspector, headers=headers, json=data)
            
            
            
        
            # line_bot_api.reply_message(
            #     event.reply_token,
            #     TextSendMessage("こちらが撮影した画像です:"))
            # #送信
            # res = requests.post(notify_url,
            #                     data=send_data,
            #                     headers=headers,
            #                     files=files)
            # print(res)#メッセージがが送れたかどうかの結果を表示

    # else:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage('メッセージありがとうございます。'))
