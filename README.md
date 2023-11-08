# Weather-Checker
A command line tool to check the weather.

## Description

A command line tool to check the current weather in your location or a given location as well as the weather forecast for the next 5 days.

## Getting Started

### Dependencies

* Python
* requests
* geocoder
* datetime
* openweathermap API

### Installing

* Simply open a command line interface at the weather_checker.py file's location.
* It is recommended to get an API key from https://openweathermap.org and subsitute it into the code.

### Executing program

* The tool can be run on its own to give the user the weather for their current location.
* adding -h shows a help section
* adding -l [Location] to the command shows the weather for the given location.
* adding -f shows the forcast for the location. -l [Location} can be omitted to show data for the users location.
* the user can add -temp, -pressure, -humidity, or -wind after -f to show the forecast for specific data
```
py weather_checker.py
py weather_checker.py -h
py weather_checker.py -l London
py weather_checker.py -l London -f
py weather_checker.py -l London -f -temp
```

## Help

If you are inputting a location with a space in it, put it in quotation marks.
```
py weather_checker.py -l "New York"
```

## Authors

Juraj Borka
