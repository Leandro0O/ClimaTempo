from lib2to3.pgen2 import token
import requests, json, datetime

class Tempo:

    def __init__(self, cidade):
        self.cidade = cidade


    def pesquisa(self):
        
        token = "bdd183e21246b328fde15eb9a0cb0107"
        url_base = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=pt_br".format(
            self.cidade, token)

        url = requests.get(url_base)
        urlJ = json.loads(url.text)

        desc = urlJ["weather"][0]['description']
        temp = int(float(urlJ["main"]["temp"]) - 273.15)
        tmin = int(float(urlJ["main"]["temp_min"]) - 273.15)
        tmax = int(float(urlJ["main"]["temp_max"]) - 273.15)
        sens = int(float(urlJ["main"]["feels_like"]) - 273.15)
        umi = int(urlJ["main"]["humidity"])
        icon = urlJ["weather"][0]["icon"]
        hora = datetime.datetime.now().time().strftime("%H : %M")
        previsao = {
              'desc':desc, 'temp':temp, 'tmin':tmin, 'tmax':tmax, 'sens':sens, 'umi':umi, 'icon':icon, 'hora': hora
           }

        return  previsao
