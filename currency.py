import requests
import os
from bs4 import BeautifulSoup

USD = 'https://www.profinance.ru/currency_usd.asp'
EUR = 'https://www.profinance.ru/currency_eur.asp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def choice():
    os.system('cls' if os.name == 'nt' else 'clear')
    first = str(input("Конвертатор валют © leish0n6\n\nЕсли вы хотите узнать курс USD/EUR/RUB к USD/EUR/RUB, то введите сокращение той валюты, курс которой вы хотите узнать к другой.\n\n(Если вы хотите конвертировать USD/EUR/RUB в USD/EUR/RUB, то оставьте поле пустым): ")).upper()

    if first == "USD":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Конвертатор валют © leish0n6\n')
        choice_f_usd = str(input("С какой валютой вы хотите посмотреть курс: Рубль (RUB): ")).upper()

        if choice_f_usd == "RUB":
            page_usd = requests.get(USD, headers=headers)
            soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
            convert_usd = soup_usd.findAll('font', {'color': 'Red'})
            res_usd = convert_usd[3].text
            final_usd = float(res_usd)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Текущий курс USD/RUB:", round(final_usd, 2), "₽")


            result = int(input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()

        else:
            choice()



    elif first == "EUR":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Конвертатор валют © leish0n6\n')
        choice_f_eur = str(input("С какой валютой вы хотите посмотреть курс: Рубль (RUB): ")).upper()

        if choice_f_eur == "RUB":
            page_eur = requests.get(EUR, headers=headers)
            soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
            convert_eur = soup_eur.findAll('font', {'color': 'Red'})
            res_eur = convert_eur[3].text
            final_eur = float(res_eur)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Текущий курс EUR/RUB:", round(final_eur, 2), '₽')

            result = int(input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()

        else:
            choice()


    elif first == "RUB":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Конвертатор валют © leish0n6\n')
        choice_f_rub = str(input("С какой валютой вы хотите посмотреть курс: Доллар (USD), Евро (EUR): ")).upper()

        if choice_f_rub == "USD":
            page_usd = requests.get(USD, headers=headers)
            soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
            convert_usd = soup_usd.findAll('font', {'color': 'Red'})
            res_usd = convert_usd[3].text
            usd_half = float(res_usd)
            final_usd = 1 / usd_half
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Текущий курс RUB/USD:", round(final_usd, 3), "₽")

            result = int(
                input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()

        elif choice_f_rub == "EUR":
            page_eur = requests.get(EUR, headers=headers)
            soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
            convert_eur = soup_eur.findAll('font', {'color': 'Red'})
            res_eur = convert_eur[3].text
            eur_half = float(res_eur)
            final_eur = 1 / eur_half
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Текущий курс RUB/USD:", round(final_eur, 3), "₽")

            result = int(
                input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()

        else:
            choice()

    else:
        convertation()


def convertation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Конвертатор валют © leish0n6\n')
    cur = str(input(
        "Введите код валюты из которой вы хотите совершить конвертацию: Доллар (USD), Евро (EUR), Рубль (RUB): ")).upper()

    if cur == "USD":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Конвертатор валют © leish0n6\n')
        choice_usd = str(input("Введите код валюты в которую вы хотите совершить конвертацию: Рубль (RUB): ")).upper()

        if choice_usd == "RUB":
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            money = float(input("Введите количество долларов ($): "))
            page_usd = requests.get(USD, headers=headers)
            soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
            convert_usd = soup_usd.findAll('font', {'color': 'Red'})
            res_usd = convert_usd[3].text
            final_usd = float(res_usd)
            cash = final_usd * money
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Введеные доллары в рублях:", round(cash, 2), "₽")
            result = int(
                input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()
            else:
                ()

        else:
            convertation()


    elif cur == "EUR":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Конвертатор валют © leish0n6\n')
        choice_eur = str(input("Введите код валюты в которую вы хотите совершить конвертацию: Рубль (RUB): ")).upper()

        if choice_eur == "RUB":
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            money = float(input("Введите количество евро (€): "))
            page_eur = requests.get(EUR, headers=headers)
            soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
            convert_eur = soup_eur.findAll('font', {'color': 'Red'})
            res_eur = convert_eur[3].text
            final_eur = float(res_eur)
            cash = money * final_eur
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Введенные евро в рублях:", round(cash, 2), '₽')
            result = int(
                input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()
            else:
                ()
        else:
            convertation()



    elif cur == "RUB":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Конвертатор валют © leish0n6\n')
        choice_rub = str(
            input("Введите код валюты в которую вы хотите совершить конвертацию: Доллар (USD), Евро (EUR): ")).upper()

        if choice_rub == "USD":
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            money = float(input("Введите количество рублей (₽): "))
            page_usd = requests.get(USD, headers=headers)
            soup_usd = BeautifulSoup(page_usd.content, 'html.parser')
            convert_usd = soup_usd.findAll('font', {'color': 'Red'})
            res_usd = convert_usd[3].text
            final_usd = float(res_usd)
            cash = money / final_usd
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Введеные рубли в долларах:", round(cash, 2), "$")
            result = int(
                input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()
            else:
                ()

        elif choice_rub == "EUR":
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            money = float(input("Введите количество рублей (₽): "))
            page_eur = requests.get(EUR, headers=headers)
            soup_eur = BeautifulSoup(page_eur.content, 'html.parser')
            convert_eur = soup_eur.findAll('font', {'color': 'Red'})
            res_eur = convert_eur[3].text
            final_eur = float(res_eur)
            cash = money / final_eur
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Конвертатор валют © leish0n6\n')
            print("Введенные рубли в евро:", round(cash, 2), '€')
            result = int(input('\nЧтобы закрыть программу - введите "0". Чтобы перезапустить программу - введите "1": '))

            if result == 0:
                ()
            elif result == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                choice()
            else:
                ()
        else:
            convertation()



    else:
        convertation()

choice()

