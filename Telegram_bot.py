import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('85274d085bebf209459af56867d11b56', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("5792215506:AAHXCoThuy6EIL9G1aPDu7bp51V3oz2og-c")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас: " + str(temp) + "  C" + "\n\n"

    if temp < 10:
        answer += "Сейчас очень холодно, одевай пуховик и шапку!"
    elif temp < 20:
        answer += "Сейчас прохладно, одевайтесь потеплее"
    else:
        answer += "На улице тепло, одевайте шорты и футболку"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
