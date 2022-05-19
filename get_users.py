from read_config import Config
import requests
import json

read_config = Config()
users_api = read_config.load()['users_api']
appToken = read_config.load()['appToken']

users = {
        "appToken": appToken,
        "page": 1,
        "pageSize": 50
}

class Users:
    def get_users(self):
        x = requests.get(users_api, params=users)
        y = json.loads(x.text)['data']['records']
        user_list = []
        for user in y:
            user_list.append(user['uid'])
        return user_list
