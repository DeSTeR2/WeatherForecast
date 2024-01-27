import requests

apiKey = '3f66088fe0f46c4c525d9fa54b3dcb84'
baseUrl = "http://api.weatherapi.com/v1"

r = requests.get('https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=39.099724&lon=-94.578331&dt=1643803200&appid=' + apiKey, auth=('user', 'pass'))
print(r.text)