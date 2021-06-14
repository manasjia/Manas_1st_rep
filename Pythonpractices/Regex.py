import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
pattern = re.compile(r'^\<T cd\>')

url = 'https://www.mohfw.gov.in/'
request_data = requests.get(url).text
soup = BeautifulSoup(request_data, "html.parser")
content_data = pattern.findall(request_data)
print(content_data)

