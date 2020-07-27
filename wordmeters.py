import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

data = []
headers = []

url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find("table", attrs={"id": "main_table_countries_today"})
table_body = table.find('tbody')
rows = table_body.find_all('tr')


""" for row in table.find_all('th'):
    header = row.getText().strip()
    data.append(header)
    headers.append(header) """

for row in rows:
    colss = row.find_all('td')
    cols = [element.text.strip() for element in colss]
    data.append([element for element in cols])


headers =[['Number', 'Country',  'TotalCases', 'NewCases', 'Total Deaths', 'New Deaths',
        'Total Recovered', 'NewRecovered', 'Active Cases', 'Serious', 'Critical',
        'Tot Cases/1M pop', 'Deaths/1M pop', 'Total Tests', 'Tests/1M pop', 'Population',
        'Continent', '1 Caseevery X ppl', '1 Deathevery X ppl']]


general_statistics_by_continent = np.concatenate((headers, data), axis=0)
print(general_statistics_by_continent)




