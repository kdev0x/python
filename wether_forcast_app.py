

import requests
from datetime import datetime






location = input("enter city name")


if location is None:
   raise ValueError("please enter a city")
api_key = "c6af695e45b0d90e5778bdc480c6a4dd"
api_link  =f" https://api.openweathermap.org/data/2.5/weather?q={location}&appid={'c6af695e45b0d90e5778bdc480c6a4dd'}"
complete_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={'c6af695e45b0d90e5778bdc480c6a4dd'}"



if ['cod'] == 404 :
   raise ValueError("sorry invalid city please add a other city")


api_response = requests.get(api_link)
api_data = api_response.json()


temp_city =((api_data["main"]["temp"]-273.15))
weather_desc = api_data['weather'][0]["description"]
hmdt = api_data["main"]["humidity"]
wind_spd = api_data["wind"]["speed"]
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")




##eror checking#










print("------------------------------------------------------------")#this print statments is for desighn benfits
print("weather stats for -{} || {}".format(location.upper(), date_time))
print("------------------------------------------------------------")
print("current temperature is: {:.2f} deg C".format(temp_city))
print("current weather desc  :",weather_desc)
print("current hummdity  :",hmdt, "%")
print("current wind speed  :", wind_spd,"kmph")





