from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

"""
    Opens site page for a given url
    converts page contents to a beautiful soup object for later use
"""
class GetSite:
    
    def __init__(self, site):
        self.driver = webdriver.Firefox()
        self.driver.get(site)
        time.sleep(1)
        self.soup = BeautifulSoup(self.driver.page_source,"html.parser")
        self.driver.close()
    
    def get_soup(self):
        return self.soup