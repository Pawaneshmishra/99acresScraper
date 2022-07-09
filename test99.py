from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup as bs

class _99Scraper:
    def __init__(self):
        self.driver = ''
        self.Description = []
        self.Location_Bldng_name = []
        self.Seller_name = []
        self.Price = []
        self.Price_unit = []
        self.Area = []
        self.Type_area = []
    
    def start_driver(self):
        self.driver = webdriver.Chrome('H:\DOWNLOADS\chromedriver.exe')

    def close_driver(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)
        
    def open_new(self,keyword):
        page = self.driver.get("https://www.99acres.com/search/property/buy/"+keyword+"?city=12&keyword=mumbai&preference=S&area_unit=1&budget_min=0&res_com=R")
        
        for i in range(1,10):
            self.driver.execute_script("window.scrollBy(0,1000)")
        content = self.driver.page_source
        soup = bs(content)

        # self.Location_Bldng_name.append(soup.findAll('td', attrs = {'class' : 'list_header_bold srpTuple__spacer10'}))

        # self.Seller_name.append(soup.findAll('div', attrs = {'class' : 'list_header_semiBold'}))

        # self.Description.append(soup.findAll('div', attrs = {'class' : 'srpTuple__descMore body_med'}))

        # self.Type_area.append(soup.findAll('div', attrs = {'class' : 'caption_subdued_small',
        #                                             'id' : 'srp_tuple_secondary_area'}))

        # self.Price.append(soup.findAll('td', attrs = {'class' : 'srpTuple__midGrid title_semiBold srpTuple__spacer16',
        #                                         'id' : 'srp_tuple_price'}))

        # self.Price_unit.append(soup.findAll('td', attrs = {'class' : 'srpTuple__midGrid title_semiBold srpTuple__spacer16',
        #                                         'id' : 'srp_tuple_price'}))

        # self.Area.append(soup.findAll('td', attrs = {'class' : 'ssrpTuple__col title_semiBold',
        #                                         'id' : 'srp_tuple_primary_area'}))
        
    
    def qa(self):
        pass
        

if __name__ == "__main__":
    scraper = _99Scraper()
    scraper.start_driver()
    keyword = "Mumbai"
    scraper.open_new(keyword)
    # scraper.qa()
    scraper.close_driver()