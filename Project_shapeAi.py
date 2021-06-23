import requests
#import os
from datetime import datetime

api_key = '88525598d371dba3025e6b852e211052'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
temp_minimum = api_data['main']['temp_min']

y=open("E:\Project\output.txt",'a')
print("-------------------------------------------------------------",file=y)
print("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=y)
print("-------------------------------------------------------------",file=y)
print ("Current temperature is: {:.2f} deg C".format(temp_city),file=y)
print("Current weather desc  :",weather_desc,file=y)
print("Current Humidity      :",hmdt, '%',file=y)
print("Current wind speed    :",wind_spd ,'kmph',file=y)
print("the minimum temperature is :",temp_minimum,'k',file=y)
y.close()
#it gives the records in output.txt file 
#we can see in the output.txt 



