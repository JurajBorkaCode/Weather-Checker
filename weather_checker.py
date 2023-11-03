import requests
import geocoder
import sys

args = sys.argv

api_key = "5d5aa43775d587efdea916f26a04b01e"

loc = ""
forecast = 0

lat = ""
lon = ""

if "-l" in args:
    index = args.index("-l")
    loc = args[index+1]

if "-f" in args:
    forecast = 1

if "-h" in args:
    print("This script shows the weather in the command line")
    print("The user can use the script to see the weather for their location")
    print("The user can use -l [location] to see the weather for a location")
    print("The user can use -f to see the forecast for a location")

    sys.exit()

def location(loc:str):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={loc}&limit=5&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        return data[0]["lat"], data[0]["lon"]
    else:
        print("Error")



def get_data(lat:str,lon:str):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error")

def get_forecast(lat:str,lon:str):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error")


g = geocoder.ip('me')

temp = None
if loc == "":
    g = geocoder.ip('me')
    temp = g.latlng
else:
    temp = location(loc)

lat = temp[0]
lon = temp[1]

if forecast == 0:
    data = get_data(lat,lon)
    print(f'Weather    | {data["weather"][0]["main"]}')
    print(f'temperature| {round(data["main"]["temp"] - 273.15,2)} °C')
    print(f'pressure   | {data["main"]["pressure"]} hPa')
    print(f'humidity   | {data["main"]["humidity"]} %')
    print(f'wind       | {data["wind"]["speed"]} m/s')
else:
    data = get_forecast(lat,lon)
