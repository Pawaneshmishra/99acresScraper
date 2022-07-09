from bs4 import BeautifulSoup as bs
from selenium import webdriver 
from requests import get
import itertools
import json

headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})


driver = webdriver.Chrome('H:\DOWNLOADS\chromedriver.exe')
driver.get("https://www.99acres.com/search/property/buy/Mumbai?city=12&keyword=mumbai&preference=S&area_unit=1&budget_min=0&res_com=R")
for i in range(1,10):
            driver.execute_script("window.scrollBy(0,1000)")
    
content = driver.page_source
soup = bs(content)
# print(html_soup.findAll('a',attrs={'class':'body_med srpTuple__propertyName','id':'srp_tuple_property_title'}))

for i in soup.findAll('a',attrs={'class':'body_med srpTuple__propertyName','id':'srp_tuple_property_title'}):
    print(i.h2.text)
    print("\n")