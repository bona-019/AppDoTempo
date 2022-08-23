import requests

class Weather():
    def __init__(self, cidade, units, lang):
        self.API_KEY = '851c344f600932ac7a62bb8a26c4dbe0'
        self.cidade = cidade
        self.units = units
        self.lang = lang
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={self.cidade}&units={self.units}&lang={self.lang}&appid={self.API_KEY}'
        self.r = requests.get(self.url).json()

    def showDesc(self):
        return self.r['weather'][0]['description'].capitalize()

    def showTemp(self):
        return str(round(self.r['main']['temp'])) + "°C"

    def showSense(self):
        return str(round(self.r['main']['feels_like'])) + "°C"

    def showTempMin(self):
        return str(round(self.r['main']['temp_min'])) + "°C"

    def showTempMax(self):
        return str(round(self.r['main']['temp_max'])) + "°C"