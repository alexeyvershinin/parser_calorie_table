import requests
import fake_useragent


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
