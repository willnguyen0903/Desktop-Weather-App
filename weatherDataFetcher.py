# import required modules
import requests, json

class weatherData:
    def __init__(self):
        pass

    def getWeatherInfo(self, city):
        # base_url variable to store url
        myApi = "0d8cfdf2a02be2b220542b4888c7fe37"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        
        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + myApi + "&q=" + city

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object 
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            temp = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding 
            # to the "description" key at 
            # the 0th index of z
            weather_description = z[0]["description"]
        else:
            return None
        return temp
        
    
"""
myTemp = weatherData()
temperature = myTemp.getWeatherInfo("sussex") - 273.15
print(f"It is {temperature:.2f} °C ")
"""
