import json
import requests
import fake_useragent
from bs4 import BeautifulSoup


url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
# генерируем рандомный User-Agent
ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random
}

req = requests.get(url, headers=headers)
page = req.text

# сохраняем полученную страницу в файл
with open('index.html', 'w', encoding="utf-8") as file:
    file.write(page)

with open('index.html', encoding="utf-8") as file:
    page_prod = file.read()

# создаем объект soup
soup = BeautifulSoup(page_prod, 'lxml')

# получаем все ссылки на группы продуктов
all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
all_categories_dict = {}

# приводим полученные данные к виду "Продукт: ссылка"
for item in all_products_hrefs:
    item_text = item.text
    item_href = 'https://health-diet.ru' + item.get('href')
    all_categories_dict[item_text] = item_href

# сохраняем данные в json
with open('all_categories_dict.json', 'w', encoding='utf-8') as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
