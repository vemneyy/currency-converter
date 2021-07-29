import requests
from bs4 import BeautifulSoup

USD = 'https://www.profinance.ru/currency_usd.asp'
EUR = 'https://www.profinance.ru/currency_eur.asp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

first = str(input("Конвертатор валют\n\nЕсли вы хотите узнать курс рубля к USD/EUR, то введите USD или EUR аналогично.\n\n(Если вы хотите конвертировать рубли в представленные валюты, то оставьте поле пустым): "))
final = first.upper()

if final == "USD":
        page_usd = requests.get(USD, headers=headers)
        soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
        convert_usd = soup_usd.findAll('font', {'color': 'Red'})
        res_usd = convert_usd[3].text
        final_usd = float(res_usd)
        print("Текущий курс USD/RUB:", round(final_usd, 2), "₽")

elif final == "EUR":
        page_eur = requests.get(EUR, headers=headers)
        soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
        convert_eur = soup_eur.findAll('font', {'color': 'Red'})
        res_eur = convert_eur[3].text
        final_eur = float(res_eur)
        print("Текущий курс EUR/RUB:", round(final_eur, 2), '₽')

else:

    cur = str(input("\nВведите код валюты для конвертации: Доллар ($): USD, Евро (€): EUR: "))
    final_cur = cur.upper()

    if final_cur == "USD":
        money = float(input("\nВведите количество ваших рублей (₽): "))
        page_usd = requests.get(USD, headers=headers)
        soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
        convert_usd = soup_usd.findAll('font', {'color': 'Red'})
        res_usd = convert_usd[3].text
        final_usd = float(res_usd)
        cash = money / final_usd
        print("\nВаши рубли в долларах:", round(cash, 2), "$")

    elif final_cur == "EUR":
        money = float(input("\nВведите количество ваших рублей (₽): "))
        page_eur = requests.get(EUR, headers=headers)
        soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
        convert_eur = soup_eur.findAll('font', {'color': 'Red'})
        res_eur = convert_eur[3].text
        final_eur = float(res_eur)
        cash = money / final_eur
        print("\nВаши рубли в евро:", round(cash, 2), '€')


    else:
        print("Error")
