import json
from opencc import OpenCC
import requests

cc = OpenCC('s2tw')

class Chat:

    def chat(messageContent):
        root = requests.get(f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={messageContent}")
        data = json.loads(root.text)
        msg = cc.convert(data["content"])
        msg = msg.replace("中國","台灣")
        msg = msg.replace(r"{face:8}",":rage:")
        return msg

    def oneMessage():
        root = requests.get("https://v1.hitokoto.cn/?c=d")
        data = json.loads(root.text)
        msg = cc.convert(data["hitokoto"])
        source = cc.convert(data["from"])
        return f"{source}：{msg}"