import requests
from bs4 import BeautifulSoup
import datetime
from rich.console import Console
from rich.table import Table


URL = 'http://www.cbr.ru/currency_base/daily/'
req = requests.get(URL)
data = req.text

soup = BeautifulSoup(data, 'html.parser')

table = soup.findAll('td')

# Искусственная индексация всех строк таблицы, содержащей курсы всех валют, для обращения к нужной валюте.
'''count = 0
for i in table:
    print(count)
    print(i)
    count += 1
'''


text_dollar = table[53]
text_dollar = text_dollar.text
value_dollar = table[54]
value_dollar = value_dollar.text

text_euro = table[58]
text_euro = text_euro.text
value_euro = table[59]
value_euro = value_euro.text

text_uan = table[83]
value_uan = table[84]
text_uan = text_uan.text
value_uan = value_uan.text


table = Table(title="Данные с ЦБР")

table.add_column("Валюта")
table.add_column("Курс")

table.add_row(text_dollar, value_dollar)
table.add_row(text_euro, value_euro)
table.add_row(text_uan, value_uan)

console = Console()
console.print(table)

dt = datetime.datetime.now()
dt_string = dt.strftime("Дата: %d/%m/%Y\nВремя: %H:%M:%S")
print(dt_string)





