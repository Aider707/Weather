import telebot
import settings
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict ['language'] = 'ru'
owm = OWM( '5371c3dc6f9beb8bd28cf283e15f9a0c', config_dict )
mgr = owm.weather_manager()

bot = telebot.TeleBot( settings.API_KEY )

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, " Привет. В каком городе узнать погоду? ")

@bot.message_handler(content_types=['text'])
def send_echo( message):
	observation = mgr.weather_at_place( message.text )
	weather = observation.weather
	weather.detailed_status

	# Скорость ветра
	wind_dict_in_meters_per_sec = observation.weather.wind()
	wind_dict_in_meters_per_sec['speed']

	# Давление
	pressure_dict = mgr.weather_at_place('place').weather.barometric_pressure()
	pressure_dict['press']

	# Температура в Цельсиях
	temp1 = weather.temperature("celsius")
	# Температура ( Чувствуется как )
	tp1 = temp1['temp']
	tp2 = temp1['feels_like']

	# Скорость ветра
	wd = wind_dict_in_meters_per_sec['speed']

	# Давление
	pr = pressure_dict['press']
	a = '\u00b0'  # Градусы
	b = '\u2735'  # Звезда

	answer = b + ' В городе ' + message.text + ' сейчас ' + str(weather.detailed_status) + '. \n' + b + 'Температура воздуха ' + str(tp1) + ' ' + a + 'C' '.\n' + b + 'Чувствуется как ' + str(tp2) + ' ' +  a + 'С. \n'
	answer += b + 'Скорость ветра ' + str(wd) + ' м/с. \n' + b + 'Давление воздуха ' + str(pr) + ' мм. рт. ст. \n\n '

	if tp1 < 10:
		answer += 'Сейчас очень холодно, одевайся как "капуста"'
	elif tp1 < 20:
		answer += "Сейчас холодно, одевайся потеплее"
	else:
		answer += "Погода теплая, одевай что хочешь"

	bot.send_message( message.chat.id, answer )
bot.infinity_polling()