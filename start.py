import time
import pandas as pd


from weather import Weather
from get_site import GetSite
from datetime import date,timedelta

from random import randint

dates = pd.read_csv("data/dates.txt")
print(dates)


class Day:
    def __init__(self, date, weather, num_of_bookings):
        self.date = date.strftime("%d/%m/%Y")
        self.weather = weather
        self.num_of_bookings = num_of_bookings

    def __str__(self):
        return f"On {self.date}\
\nthere are {self.num_of_bookings} left\n\
forcast: {self.weather.weather}, Temp: {self.weather.min_temp} - {self.weather.max_temp}"
#pd.DataFrame(columns=["ID","date"])
    def add_to_data(self, date_data):
        if pd.to_datetime(self.date) not in date_data:
            pass
        day = pd.DataFrame({})


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
    days.append(Day(the_date, weather, num))
    the_date += delta

for day in days:
    print(day)
    print()