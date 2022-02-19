import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def burnable():
    # USER_ID = info['USER_ID']
    messages = TextSendMessage(text="おはよう〜！ \n今日は燃えるゴミの日やで〜！\n捨てるの忘れんようにな！" )
    line_bot_api.broadcast(messages=messages)
    

if __name__ == "__main__":
    burnable()