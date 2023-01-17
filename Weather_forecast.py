from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('85274d085bebf209459af56867d11b56', config_dict)
mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас - " + str(temp) + "  C")
