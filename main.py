import requests
from bs4 import BeautifulSoup
import datetime


URL = 'https://meteoinfo.ru/forecasts/russia/moscow-area/moscow'
req = requests.get(URL)
data = req.text

soup = BeautifulSoup(data, 'html.parser')

table = soup.find('span', class_="fc_temp_short")
Moscow_temp = table
Moscow_temp = Moscow_temp.text

dt = datetime.datetime.now()
dt_string = dt.strftime("Дата: %d/%m/%Y\n")

print(' В Москве\n', dt_string, Moscow_temp)
