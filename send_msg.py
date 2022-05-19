from read_config import Config
import requests
from get_qinghua import Qinghua
from get_users import Users

read_config = Config()
send_api = read_config.load()['send_api']
appToken = read_config.load()['appToken']

class Msg:
    def __init__(self):
        self.uids = Users().get_users() #get uid list
        self.qinghua = Qinghua().get_qinghua() #get a random 土味情话

        self.custom_header = {"Content-Type":"application/json"}

        self.msg = {
                "appToken": appToken,
                "content": self.qinghua,
                "summary":"土味情话已送达,点开看看里面是什么吧",
                "contentType":1,
                "uids": self.uids
        }

    def send_message(self):
        x = requests.post(send_api, json=self.msg, headers=self.custom_header)
        print("Send Feedback:\n", x.text)