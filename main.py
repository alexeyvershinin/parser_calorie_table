import csv
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

with open('all_categories_dict.json', encoding='utf-8') as file:
    all_categories = json.load(file)

count = 0
# на каждой итерации цикла заходим на новую страницу категории и собираем данные
for category_name, category_href in all_categories.items():

    if count == 0:
        # заменяем символы в именах категорий
        rep = [",", " ", "-", "'"]
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, '_')

        # переходим по ссылке категории и получаем данные
        r = requests.get(url=category_href, headers=headers)
        src = r.text

        # сохраняем данные в html
        with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)

        with open(f'data/{count}_{category_name}.html', encoding='utf-8') as file:
            category_page = file.read()

        soup = BeautifulSoup(category_page, 'lxml')

        # получаем заголовки таблицы
        table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')

        product = table_head[0].text
        calories = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text

        # сохраняем заголовки таблицы в файл .csv
        with open(f'data/{count}_{category_name}.csv', 'w', encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\n')
            writer.writerow(
                (
                    product,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

        count += 1
