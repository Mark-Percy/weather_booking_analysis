from get_site import GetSite

class Weather:

    def __init__(self, soup, date = None):
        self.day = date.strftime("%A")
        self.soup = soup
        self.temp = None
        self.getWeather()

    def __str__(self):
        return f"This is the weather for: {self.day} in {self.loc}: \n\
Weather: {self.weather}\
\nTemperature:\n\
    Min : {self.min_temp} -> Max : {self.max_temp}"

    def getWeather(self):
        weather_block = self.soup.find(id = "wob_wc")
        self.loc =  weather_block.find(id= "wob_loc").get_text()
        days_weather = weather_block.find(attrs = {"aria-label":self.day}).parent
        self.weather = days_weather.find("img").attrs["alt"]
        temp = days_weather.findAll("span", {"class":"wob_t"})
        self.max_temp = temp[0].get_text()
        self.min_temp = temp[2].get_text()


