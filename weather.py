from get_site import GetSite

import pandas as pd

"""
Weather object to store the weather for each day that the program is ran for.
"""

class Weather:

    #To initialise the data needed is the soup object from the site and the given date.

    def __init__(self, soup, date = None):
        self.day = date.strftime("%A")
        self.soup = soup
        self.temp = None
        self.get_weather()

    #Returns a sting version of what is in the weather object

    def __str__(self):
        return f"This is the weather for: {self.day} in {self.loc}: \n\
Weather: {self.weather_name}\
\nTemperature:\n\
    Min : {self.min_temp} -> Max : {self.max_temp}"

    # Assigns all the object variables from the inserted soup object

    def get_weather(self):
        weather_block = self.soup.find(id = "wob_wc")
        self.loc =  weather_block.find(id= "wob_loc").get_text()
        days_weather = weather_block.find(attrs = {"aria-label":self.day}).parent
        self.weather_name = days_weather.find("img").attrs["alt"]
        temp = days_weather.findAll("span", {"class":"wob_t"})
        self.max_temp = temp[0].get_text()
        self.min_temp = temp[2].get_text()
        self.weather_id = self.get_weather_id() # assigns the weather id by running the get_weather_id function

    # Finds whether the weather name is already stored: if not it adds it to the bottom of the weather file, then returns the new id, 
    # if the weather name is found then it finds the related id.

    def get_weather_id(self):
        weather_df = pd.read_csv("data/weather.txt")
        if(self.weather_name in weather_df.weather_name.values):
            idx = weather_df.index[weather_df.weather_name == self.weather_name]
            weather_id = weather_df.loc[idx].ID.values[0]
            return weather_id
        else:
            
            new_id = weather_df.iloc[-1]["ID"]+1
            weather_data = pd.DataFrame(data = {"ID" : new_id, "weather_name": [self.weather_name]})
            weather_df = weather_df.append(weather_data)
            weather_df.to_csv("data/weather.txt", index=False)