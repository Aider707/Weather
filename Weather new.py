from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict ['language'] = 'ru'
owm = OWM( '5371c3dc6f9beb8bd28cf283e15f9a0c', config_dict )

mgr = owm.weather_manager()
place = input( 'В каком городе?: ')
observation = mgr.weather_at_place('place')
weather = observation.weather
#weather.status
#weather.detailed_status
#Скорость ветра
wind_dict_in_meters_per_sec = observation.weather.wind()
wind_dict_in_meters_per_sec['speed']
# Давление
pressure_dict = mgr.weather_at_place('place'). weather.barometric_pressure()
pressure_dict ['press']
#Температура в Цельсиях
temp1 = weather.temperature("celsius")
#Температура (показатели разные)
tp1 = temp1['temp']
tp2 = temp1['feels_like']
#Скорость ветра
wd = wind_dict_in_meters_per_sec['speed']
# Давление
pr = pressure_dict ['press']
a = '\u00b0'  # Градусы
b = '\u2735'  #Звезда
print(b + ' В городе ' + place + ' сейчас ' + str(weather.detailed_status) + '.' + ' Температура ' + str(tp1) +' '+ a + 'C, чувствуется как ' + str( tp2 ) + ' ' + a + 'C')
print( 'Скорость ветра ' + str(wd) + ' м/с. \nДавление ' + str(pr) + ' мм.рт.ст. \n')

if tp1 < 10:
    print( "Сейчас холодно,одевайся потеплее" )
elif tp1 < 20:
    print( "Не сильно холодно, одевайся как хочешь" )