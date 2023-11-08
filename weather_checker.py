import requests
import geocoder
import sys
import datetime

args = sys.argv

api_key = "5d5aa43775d587efdea916f26a04b01e"

loc = ""

lat = ""
lon = ""

if "-l" in args:
    index = args.index("-l")
    loc = args[index+1]


if "-h" in args:
    print("This script shows the weather in the command line")
    print("The user can use the script to see the weather for their location")
    print("The user can use -l [location] to see the weather for a location")
    print("The user can use -f to see the weather forecast for a location")
    print("The user can add a modifier after -f to see different forecast values for a location")
    print("The modifiers are:")
    print(" -temp")
    print(" -pressure")
    print(" -humidity")
    print(" -wind")

    sys.exit()

def location(loc:str):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={loc}&limit=5&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        return data[0]["lat"], data[0]["lon"]
    else:
        print("API key Error")



def get_data(lat:str,lon:str):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("API key Error")

def get_forecast(lat:str,lon:str):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("API key Error")


g = geocoder.ip('me')

temp = None
if loc == "":
    g = geocoder.ip('me')
    temp = g.latlng
else:
    temp = location(loc)

lat = temp[0]
lon = temp[1]

if "-f" not in args:
    data = get_data(lat,lon)
    print(f'weather    | {data["weather"][0]["main"]}')
    print(f'temperature| {round(data["main"]["temp"] - 273.15,2)} °C')
    print(f'pressure   | {data["main"]["pressure"]} hPa')
    print(f'humidity   | {data["main"]["humidity"]} %')
    print(f'wind       | {data["wind"]["speed"]} m/s')
else:
    data = get_forecast(lat,lon)

    date = datetime.datetime.today()

    dates = []
    for x in range(0, 6):
        day = str(date + datetime.timedelta(days=x))
        date_only = day.split(" ")[0]
        day_only = date_only.split("-")[2]
        dates.append(day_only)

    #format_data
    formatted_data = {dates[0]:{"00:00:00":["","","","",""],"03:00:00":["","","","",""],"06:00:00":["","","","",""],"09:00:00":["","","","",""],"12:00:00":["","","","",""],"15:00:00":["","","","",""],"18:00:00":["","","","",""],"21:00:00":["","","","",""]},
                    dates[1]:{"00:00:00":[],"03:00:00":[],"06:00:00":[],"09:00:00":[],"12:00:00":[],"15:00:00":[],"18:00:00":[],"21:00:00":[]},
                    dates[2]:{"00:00:00":[],"03:00:00":[],"06:00:00":[],"09:00:00":[],"12:00:00":[],"15:00:00":[],"18:00:00":[],"21:00:00":[]},
                    dates[3]:{"00:00:00":[],"03:00:00":[],"06:00:00":[],"09:00:00":[],"12:00:00":[],"15:00:00":[],"18:00:00":[],"21:00:00":[]},
                    dates[4]:{"00:00:00":[],"03:00:00":[],"06:00:00":[],"09:00:00":[],"12:00:00":[],"15:00:00":[],"18:00:00":[],"21:00:00":[]},
                    dates[5]:{"00:00:00":[],"03:00:00":[],"06:00:00":[],"09:00:00":[],"12:00:00":[],"15:00:00":[],"18:00:00":[],"21:00:00":[]}}

    

    for data_point in data["list"]:
        data_point_dt = str(data_point["dt_txt"]).split(" ")
        day_in_point = data_point_dt[0].split("-")[2]
        time_in_point = data_point_dt[1]

        input_data = []

        input_data.append(data_point["weather"][0]["main"])
        input_data.append(f'{round(data_point["main"]["temp"] - 273.15,2)}°C')
        input_data.append(f'{data_point["main"]["pressure"]} hPa')
        input_data.append(f'{data_point["main"]["humidity"]}%')
        input_data.append(f'{data_point["wind"]["speed"]} m/s')


        formatted_data[day_in_point][time_in_point] = input_data


    #table


    selected = 0

    if "-temp" in args:
        selected = 1

    elif "-pressure" in args:
        selected = 2

    elif "-humidity" in args:
        selected = 3

    elif "-wind" in args:
        selected = 4

    print(f"{'':6}|{dates[0]:10}|{dates[1]:10}|{dates[2]:10}|{dates[3]:10}|{dates[4]:10}")
    print(f"|{'00:00':5}|{formatted_data[dates[0]]['00:00:00'][selected]:10}|{formatted_data[dates[1]]['00:00:00'][selected]:10}|{formatted_data[dates[2]]['00:00:00'][selected]:10}|{formatted_data[dates[3]]['00:00:00'][selected]:10}|{formatted_data[dates[4]]['00:00:00'][selected]:10}")
    print(f"|{'03:00':5}|{formatted_data[dates[0]]['03:00:00'][selected]:10}|{formatted_data[dates[1]]['03:00:00'][selected]:10}|{formatted_data[dates[2]]['03:00:00'][selected]:10}|{formatted_data[dates[3]]['03:00:00'][selected]:10}|{formatted_data[dates[4]]['03:00:00'][selected]:10}")
    print(f"|{'06:00':5}|{formatted_data[dates[0]]['06:00:00'][selected]:10}|{formatted_data[dates[1]]['06:00:00'][selected]:10}|{formatted_data[dates[2]]['06:00:00'][selected]:10}|{formatted_data[dates[3]]['06:00:00'][selected]:10}|{formatted_data[dates[4]]['06:00:00'][selected]:10}")
    print(f"|{'09:00':5}|{formatted_data[dates[0]]['09:00:00'][selected]:10}|{formatted_data[dates[1]]['09:00:00'][selected]:10}|{formatted_data[dates[2]]['09:00:00'][selected]:10}|{formatted_data[dates[3]]['09:00:00'][selected]:10}|{formatted_data[dates[4]]['09:00:00'][selected]:10}")
    print(f"|{'12:00':5}|{formatted_data[dates[0]]['12:00:00'][selected]:10}|{formatted_data[dates[1]]['12:00:00'][selected]:10}|{formatted_data[dates[2]]['12:00:00'][selected]:10}|{formatted_data[dates[3]]['12:00:00'][selected]:10}|{formatted_data[dates[4]]['12:00:00'][selected]:10}")
    print(f"|{'15:00':5}|{formatted_data[dates[0]]['15:00:00'][selected]:10}|{formatted_data[dates[1]]['15:00:00'][selected]:10}|{formatted_data[dates[2]]['15:00:00'][selected]:10}|{formatted_data[dates[3]]['15:00:00'][selected]:10}|{formatted_data[dates[4]]['15:00:00'][selected]:10}")
    print(f"|{'18:00':5}|{formatted_data[dates[0]]['18:00:00'][selected]:10}|{formatted_data[dates[1]]['18:00:00'][selected]:10}|{formatted_data[dates[2]]['18:00:00'][selected]:10}|{formatted_data[dates[3]]['18:00:00'][selected]:10}|{formatted_data[dates[4]]['18:00:00'][selected]:10}")
    print(f"|{'21:00':5}|{formatted_data[dates[0]]['21:00:00'][selected]:10}|{formatted_data[dates[1]]['21:00:00'][selected]:10}|{formatted_data[dates[2]]['21:00:00'][selected]:10}|{formatted_data[dates[3]]['21:00:00'][selected]:10}|{formatted_data[dates[4]]['21:00:00'][selected]:10}")
