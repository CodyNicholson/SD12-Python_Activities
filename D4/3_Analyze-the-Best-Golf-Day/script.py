#WINDOWS
# .\venv\Scripts\activate
#MAC
# source venv/bin/activate
# pip install -r requirements.txt

import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

API_URL = 'https://goweather.herokuapp.com/weather/'
city = 'seattle'

r = requests.get(API_URL + city)
response = r.json()
response = {
    'description': 'Partly cloudy',
    'forecast': [ {'day': '1', 'temperature': '+22 °C', 'wind':'12 km/h'},
                  {'day': '2', 'temperature': '+15 °C', 'wind':'14 km/h'},
                  {'day': '3', 'temperature': '+5 °C', 'wind':'4 km/h'}],
    'temperature': '21 °C',
    'wind': '9 km/h'
}

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(response)

forecast_list = response['forecast']

today = datetime.now().strftime("%b-%d-%Y")

to_graph = {}
count = 1
for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count+=1 if current_date <= 31 else 1

    day['wind'] = 0 if day['wind'][0] == ' ' else int(day['wind'][:2])

    to_graph[this_day] = day['wind']

print('to_graph dictionary: ', to_graph)

plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')

print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())
plt.scatter(to_graph.keys(), to_graph.values())
plt.show()
