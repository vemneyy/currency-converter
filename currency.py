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
