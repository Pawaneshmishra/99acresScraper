from bs4 import BeautifulSoup as bs
import translators as ts
from selenium import webdriver 
import time

class dailyThantiScraper:
    def __init__(self):
        self.driver = ''
        self.heading = []
        self.details = []
        self.time_date = []
        self.soup = ''
    
    def start_driver(self):
        self.driver = webdriver.Chrome('H:\DOWNLOADS\chromedriver.exe')

    def open_url(self, url):
        self.driver.get(url)
        
    def open_new(self):
        page = self.driver.get("https://www.dailythanthi.com/chennai")
        html = self.driver.page_source
        self.soup = bs(html,'html.parser')
        
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)


    def get_data(self):
        data = self.soup.findAll('div',attrs={'class':'ListingNewsWithMEDImage'})
        for div in data:
            self.heading.append(div.h3.text)
            self.details.append(div.div.text)
            self.time_date.append(div.span.text)

    def translate_data(self):
        for i in range(len(self.heading)):
            self.heading[i] = ts.google(self.heading[i],from_language='ta',to_language='en')
       
        for i in range(len(self.details)):
            self.details[i] = ts.google(self.details[i],from_language='ta',to_language='en')
        
        # print(self.heading[1],self.details[1],self.time_date[1])

if __name__ == "__main__":
    scraper = dailyThantiScraper()
    scraper.start_driver()
    scraper.open_new()
    scraper.get_data()
    scraper.translate_data()