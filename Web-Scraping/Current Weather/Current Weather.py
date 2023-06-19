import requests, json
api_key = "< openweathermap - web api key used >"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url).json()

a = response.keys()
for i in a:
    print(f" {i} = {response[i]}")
    
