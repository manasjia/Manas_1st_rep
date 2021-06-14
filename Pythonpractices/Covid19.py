import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://www.mohfw.gov.in"
response = requests.get(url).text
soup = BeautifulSoup(response,"html.parser")
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
header_data= soup.find_all('tr', recursive=True)

state_data = []
for head in header_data:
    heads = extract_contents(head.find_all('td'))
    if len(heads) == 5:
        state_data.append(heads)
#print(state_data)
new_cols = ["Srno","States","Confirmed","Recovered","Deceased"]
result_data = pd.DataFrame(data=state_data, columns=new_cols)

#print(result_data.head())
result_data['Confirmed'] = result_data['Confirmed'].map(int)
result_data['Recovered'] = result_data['Recovered'].map(int)
result_data['Deceased'] = result_data['Deceased'].map(int)


table = PrettyTable()
table.field_names= (new_cols)
for i in state_data:
    table.add_row(i)
table.add_row(["", "Total", sum(result_data['Confirmed']), sum(result_data['Recovered']), sum(result_data['Deceased'])])
print(table)

##plot graph

sns.set_style("ticks")
plt.figure(figsize=(15,10))
plt.barh(result_data['States'], result_data['Confirmed'].map(int), align = 'center', color = 'lightblue', edgecolor = 'blue')
plt.xlabel('No. of Confirmed cases', fontsize = 18)
plt.ylabel('States/UT', fontsize = 18)
plt.gca().invert_yaxis()  # this is to maintain the order in which the states appear
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.title('Total Confirmed Cases Statewise', fontsize=20)

for index, value in enumerate(result_data["Confirmed"]):
    plt.text(value, index, str(value), fontsize =12, verticalalignment='center')
plt.show()
