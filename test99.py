from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup as bs

class _99Scraper:
    def __init__(self):
        self.driver = ''
        self.soup =''
        self.Description = []#
        self.Location_Bldng_name = []#
        self.Seller_name = []#
        self.Price = []#
        self.Area = []#
        self.Bhk = []
        self.Date_posted = []#
    
    def start_driver(self):
        self.driver = webdriver.Chrome('H:\DOWNLOADS\chromedriver.exe')

    def close_driver(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)
        
    def open_new(self,keyword):
        page = self.driver.get("https://www.99acres.com/search/property/buy/"+keyword+"?city=12&keyword=mumbai&preference=S&area_unit=1&budget_min=0&res_com=R")

        content = self.driver.page_source
        self.soup = bs(content)
    
    def get_details(self):
        for i in self.soup.findAll('a',attrs={'class':'body_med srpTuple__propertyName','id':'srp_tuple_property_title'}):
            self.Location_Bldng_name.append(i.h2.text)
        
        for i in self.soup.findAll('div',attrs={'class':'ellipsis srpTuple__smallDescriptionStyle'}):
            self.Description.append(i.text)

        for i in self.soup.findAll('div',attrs={'class':'srpTuple__postedByText list_header_semiBold Ng100 ellipsis'}):
            self.Seller_name.append(i.text)
        
        for i in self.soup.findAll('div',attrs={'class':'f10 Ng100 srpTuple__postedByText ellipsis'}):
            self.Date_posted.append(i.span.text.replace('by',''))

        for i in self.soup.findAll('td',attrs={'class':'srpTuple__col title_semiBold','id':'srp_tuple_price'}):
            self.Price.append(i.text)
        
        for i in self.soup.findAll('td',attrs={'class':'srpTuple__col title_semiBold','id':'srp_tuple_primary_area'}):
            self.Area.append(i.text)

        for i in self.soup.findAll('td',attrs={'class':'srpTuple__col title_semiBold','id':'srp_tuple_bedroom'}):
            self.Area.append(i.text)


        print(len(self.Location_Bldng_name),len(self.Description),len(self.Seller_name),len(self.Price),len(self.Area),len(self.Bhk),len(self.Date_posted))

if __name__ == "__main__":
    scraper = _99Scraper()
    scraper.start_driver()
    keyword = "Mumbai"
    scraper.open_new(keyword)
    scraper.get_details()
    scraper.close_driver()