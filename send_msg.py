from read_config import Config
import requests
from get_qinghua import Qinghua
from get_users import Users

read_config = Config()
send_api = read_config.load()['send_api']
appToken = read_config.load()['appToken']

uids = Users().get_users() #get uid list
qinghua = Qinghua().get_qinghua() #get a random 土味情话

custom_header = {"Content-Type":"application/json"}

msg = {
        "appToken": appToken,
        "content": qinghua,
        "summary":"土味情话已送达,点开看看里面是什么吧",
        "contentType":1,
        "uids": uids
}

class Msg:
    def send_message(self):
        x = requests.post(send_api, json=msg, headers=custom_header)
        print("Send Feedback:\n", x.text)




