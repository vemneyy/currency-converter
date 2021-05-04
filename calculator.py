
print()
print('Чтобы сложить нажмите- +, вычесть- -, умножить- *, разделить- /, возвести в степень- **')
print()
one = int(input('Первое число: '))
action = input('Действие: ')
two = int(input('Второе число: '))

plus = '+'
minus = '-'
multiplication = '*'
division = '/'
step = '**'
sign = ['+', '-', '*', '/', '**']

if action == plus:
    print(one + two)

elif action == minus:
    print(one - two)

elif action == multiplication:
    print(one * two)

elif action == division:
    print(one / two)

elif action == step:
    print(one ** two)

else:
    print('Введен неверный знак действия')

print()
print('Нажмите на Enter чтобы выйти...')
input()
