from bs4 import BeautifulSoup
from requests import get
import itertools
import json

headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

sapo = "https://www.99acres.com/search/property/buy/mumbai?city=12&keyword=mumbai&preference=S&area_unit=1&budget_min=0&res_com=R"
response = get(sapo, headers=headers)

html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup.find('a',attrs={'class':'body_med srpTuple__propertyName','id':'srp_tuple_property_title'}).h2.text)