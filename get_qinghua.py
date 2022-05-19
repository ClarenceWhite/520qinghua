from read_config import Config
import requests

read_config = Config()
qinghua_api = read_config.load()['qinghua_api']

format = {'format': 'text'}

class Qinghua:
    def get_qinghua(self):
        x = requests.get(qinghua_api, params=format)
        return (x.text)