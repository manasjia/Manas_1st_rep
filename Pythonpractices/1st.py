import html

import pandas as pd
from bs4 import BeautifulSoup

import requests as re


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

text = re.get('https://www.weather-forecast.com/locations/Hyderabad/forecasts/latest')
#print(text.text)

soup = BeautifulSoup(text.content, 'html.parser')
items = soup.find('div', {'class':'b-forecast__overflow'})
#print(type(items))
#print(items)
days = items.find_all('span', {'class':'b-forecast__table-days-name'})
print(days)