from lib2to3.pgen2 import token
import requests
import json, datetime


class Tempo:

    def base_url(cidade):
        token = "bdd183e21246b328fde15eb9a0cb0107"
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=pt_br".format(
            cidade, token)
        return url

    def url_json(url):
        url = requests.get(url)
        urlJ = json.loads(url.text)  
        return urlJ

    def hora():
        hora = datetime.datetime.now().time().strftime("%H : %M")
        return hora

