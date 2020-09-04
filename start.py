import time
import pandas as pd


from weather import Weather
from get_site import GetSite
from datetime import date,timedelta

from random import randint
tic = time.time()
print("Program Started")
print("-"*20)

dates = pd.read_csv("data/dates.txt")
day_data = pd.read_csv("data/day_data.txt")


class Day:
    def __init__(self, date, weather, num_of_bookings):
        self.date = date
        self.weather = weather
        self.num_of_bookings = num_of_bookings

    def __str__(self):
        return f"On {self.date}\
\nthere are {self.num_of_bookings} left\n\
forcast: {self.weather.weather_name}, Temp: {self.weather.min_temp} - {self.weather.max_temp}"


    def add_to_data(self, date_data, this_day_data):
        i_d = 0
        days_id = 0
        # adds the day to the dates dataframe if not already there
        if pd.Timestamp(self.date) not in pd.to_datetime(date_data["date"].values):
            if not date_data.empty:
                i_d = [date_data.iloc[-1]["ID"]+1]
            
            else:
                i_d = 1
            
            day = pd.DataFrame(data= {"ID": i_d ,"date": [self.date]})
            date_data = date_data.append(day)

        else:
            i_d = date_data.loc[pd.to_datetime(date_data["date"]) == pd.Timestamp(self.date), "ID"].iloc[0]

        # appends the relevant information to the day_data df for the day that is currently on.

        if(this_day_data.empty):
            days_id = 1
        else:
            days_id = [this_day_data.iloc[-1]["ID"]+1]

        temp_df = pd.DataFrame(data= {
                                    "ID" :days_id, 
                                    "date_ID":i_d,
                                    "number_of_days_until":[(self.date-date.today()).days],
                                    "weather_id":[self.weather.weather_id],
                                    "min_temp":[self.weather.min_temp],
                                    "max_temp":[self.weather.max_temp],
                                    "number_available":[self.num_of_bookings]
                                })
        this_day_data = this_day_data.append(temp_df)
        return date_data, this_day_data
    
    def add_date(self):
        pass

    def add_date_data(self):
        pass

weather_soup = GetSite("https://www.google.com/search?q=aintree+weather").get_soup()

the_date = date.today()
delta = timedelta(days=1)
days= []
weather = None

for i in range(6):
    # rand int to reduce testing time
    num = len(GetSite("https://aintree.intelligentgolf.co.uk/visitorbooking/?date=" + the_date.strftime("%d-%m-%Y")).get_soup().find_all("td", class_ = "bookable:4", style = ""))
    # num = randint(1,30)
    weather = Weather(weather_soup,the_date)
    day = (Day(the_date, weather, num))
    dates,day_data = day.add_to_data(dates, day_data)
    the_date += delta

print(day_data)

dates.to_csv("data/dates.txt", index=False)
day_data.to_csv("data/day_data.txt", index=False)
toc = time.time()

print(f"elapsed time -> {toc - tic}")