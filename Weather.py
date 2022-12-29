# Берем информацию  о погоде с стороннего сайта (который бесплатно предоставляет информацию)
import pyowm
owm = pyowm.OWM('5371c3dc6f9beb8bd28cf283e15f9a0c')
place = input( 'В каком городе?:')
observation = owm.weather_manager().weather_at_place('place')
w = observation.weather
print(w)