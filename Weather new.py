from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM( '5371c3dc6f9beb8bd28cf283e15f9a0c', config_dict )
place = input( 'В каком городе?: ')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('place')
weather = observation.weather
weather.status
weather.detailed_status
temp1 = weather.temperature("celsius")

# 20 pages from doc. Pyowm. Temperature in celsium, and wind power
print(' В городе ' + place + ' сейчас ' + str(weather) + '.' + ' Температура ' + str(temp1)+ ' С ' )

#print(weather)
