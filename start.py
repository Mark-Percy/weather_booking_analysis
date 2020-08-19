import time
import pandas as pd


from weather import Weather
from get_site import GetSite
from datetime import date,timedelta

from random import randint

dates = pd.read_csv("data/dates.txt")


class Day:
    def __init__(self, date, weather, num_of_bookings):
        self.date = date
        self.weather = weather
        self.num_of_bookings = num_of_bookings

    def __str__(self):
        return f"On {self.date}\
\nthere are {self.num_of_bookings} left\n\
forcast: {self.weather.weather}, Temp: {self.weather.min_temp} - {self.weather.max_temp}"


    def add_to_data(self, date_data):
        i_d = 0
        if pd.Timestamp(self.date) not in pd.to_datetime(date_data["date"].values):
            if not date_data.empty:
                i_d = [date_data.iloc[-1]["ID"]+1]
            else:
                i_d = 1
            
            day = pd.DataFrame(data= {"ID": i_d ,"date": [self.date]})
            date_data = date_data.append(day)
        return {"dates" : date_data}


weather_soup = GetSite("https://www.google.com/search?q=aintree+weather").get_soup()

the_date = date.today()
delta = timedelta(days=1)
days= []
weather = None
for i in range(6):
    # rand int to reduce testing time
    #num = len(GetSite("https://aintree.intelligentgolf.co.uk/visitorbooking/?date=" + the_date.strftime("%d-%m-%Y")).get_soup().find_all("td", class_ = "bookable:4"))
    num = randint(1,30)
    weather = Weather(weather_soup,the_date)
    day = (Day(the_date, weather, num))
    dates = day.add_to_data(dates)
    the_date += delta

print(dates)
dates.to_csv("data/dates.txt", index=False)