import requests
from bs4 import BeautifulSoup

USD = 'https://www.profinance.ru/currency_usd.asp'
EUR = 'https://www.profinance.ru/currency_eur.asp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

money = float(input("Введите количество рублей (₽): "))
cur = int(input("Введите код валюты (Доллар ($): 1 , Евро (€): 2): "))

if cur == 1:
    page_usd = requests.get(USD, headers=headers)
    soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
    convert_usd = soup_usd.findAll('font', {'color': 'Red'})
    res_usd = convert_usd[0].text
    final_usd = float(res_usd)

elif cur == 2:
    page_eur = requests.get(EUR, headers=headers)
    soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
    convert_eur = soup_eur.findAll('font', {'color': 'Red'})
    res_eur = convert_eur[0].text
    final_eur = float(res_eur)
else:
    ()

if cur == 1:
    cash = money / final_usd
    print("Ваши рубли в долларах:", round(cash, 2), "$")
elif cur == 2:
    cash = money / final_eur
    print("Ваши рубли в евро:", round(cash, 2), '€')
else:
    print("Error")















# import requests
# import bs4
# from bs4 import BeautifulSoup
#
# # Основной класс
# class Currency:
# 	# Ссылка на нужную страницу
# 	DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
# 	# Заголовки для передачи вместе с URL
# 	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#
# 	current_converted_price = 0
# 	difference = 5 # Разница после которой будет отправлено сообщение на почту
#
# 	def __init__(self):
# 		# Установка курса валюты при создании объекта
# 		self.current_converted_price = float(self.get_currency_price().replace(",", "."))
#
# 	# Метод для получения курса валюты
# 	def get_currency_price(self):
# 		# Парсим всю страницу
# 		full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
#
# 		# Разбираем через BeautifulSoup
# 		soup = BeautifulSoup(full_page.content, 'html.parser')
#
# 		# Получаем нужное для нас значение и возвращаем его
# 		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
# 		print(convert[0].text)
#
#
#
# euro = 85
# money = int(input("Введите количество ваших денег: "))
# cur = int(input("Введите код валюты (Доллар: 1, Евро: 2): "))
# if cur == 1:
#     cash = money / int(usd)
#     print("Вот ваш Кэш: ", round(cash, 2))
# elif cur == 2:
#     cash = money / euro
#     print("Вот ваш Кэш: ", round(cash, 2))
# else:
#     print("Error")