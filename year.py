year = input('Введите год: ')

for val in year:
    if int(year) % 4 == 0:
        print('Високосный')
        break
    else:
        print('Не високосный')
        break


