import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def remind_pet_bottles():
    # USER_ID = info['USER_ID']
    pet_bottles = '缶、瓶、ペットボトル、プラスチック'
    messages = TextSendMessage(text="お疲れさま〜！ \n明日は" + pet_bottles + "の日やで〜！\n準備しときなよ〜！" )
    line_bot_api.broadcast(messages=messages)
    

if __name__ == "__main__":
    remind_pet_bottles()