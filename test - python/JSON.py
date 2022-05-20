#---- 01
import requests

def get_response():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=0af7650b00321f8081a8a9ad3a838f51")
    return response.json()['sys']['country']

print(get_response())


#---- 02
def data():
    lst_mfr = []
    response = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json")
    a = response.json()["Results"]
    for x in a:
        if x["Country"] == "UNITED KINGDOM (UK)":
            lst_mfr.append(x["Mfr_Name"])
    return lst_mfr
print(data())


#---- 03
import requests

def data():
    url = "http://api.shoutcloud.io/V1/SHOUT"
    payload = {"INPUT":"test test"}
    response = requests.post(url, json=payload)
    return response.json()
print(data())


# ----- 04. weather
import requests

def data():
    weather_main = []
    response = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=jayapura,id&appid=27edaa711aa55803ce95bab5bdaa2129')
    a = response.json()['list'][0]['weather'][0]['main']
    b = response.json()['list'][0]['main']['temp']
    c = (response.json()['city']['coord']['lat'])
    d = (response.json()['city']['coord']['lon'])
    weather_main.append(a)
    weather_main.append(b)
    weather_main.append(c)
    weather_main.append(d)
    return weather_main
print(data())
