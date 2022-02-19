import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def remind_burnable():
    # USER_ID = info['USER_ID']
    burnable = '燃えるゴミ'
    unburnable = '燃えないゴミ、紙ゴミ、有害危険ゴミ、繊維ゴミ'
    pet_bottles = '缶、瓶、ペットボトル、プラスチック'
    messages = TextSendMessage(text="お疲れさま〜！ \n明日は" + burnable + "の日やで〜！\n準備しときなよ〜！" )
    line_bot_api.broadcast(messages=messages)
    

if __name__ == "__main__":
    remind_burnable()