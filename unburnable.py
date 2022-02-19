import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def unburnable():
    # USER_ID = info['USER_ID']
    messages = TextSendMessage(text="おはよう〜！ \n今日は燃えないゴミ、紙ゴミ、有害危険ゴミ、繊維ゴミの日やで〜！\n捨てるの忘れんようにな！" )
    line_bot_api.broadcast(messages=messages)
    
def discription():
    # USER_ID = info['USER_ID']
    message1 = TextSendMessage(text="有害危険ゴミは、「乾電池、蛍光管、水銀体温計、ライター、スプレーかん・カートリッジ式ボンベ」とかやで〜")
    line_bot_api.broadcast(messages=message1)
    

if __name__ == "__main__":
    unburnable()
    discription()
