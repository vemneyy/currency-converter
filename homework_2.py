"""Easy"""

"""
Задача №1
"""

# fruits = ['apple', 'banana', 'qiwi', 'watermelon']
# num = [1, 2, 3, 4, 5]
# print('1.', fruits[0])
# print('2.', fruits[1])
# print('3.', fruits[2])
# print('4.', fruits[3])
#
# print('1. {}'.format(fruits[0]))
#
# print(f'{num}. {fruits}')

"""
Задача №2
"""

# first = {1, 2, 7, 5, 4, 9}
# secondary = {1, 3, 8, 2, 9}
#
# print(first - secondary)

"""
Задача №3
"""

# numbers = [1, 4, 6, 7, 8, 9, 10]
#
# new = []
#
# for val in numbers:
#     if val %2 == 0:
#         new.append(int(val / 4))
#     else:
#         new.append(int(val * 2))
#
# print(new)

"""Normal"""

"""
Задача №1
"""

# numbers = [49, 2, -5, 8, 9, -25, 25, 4]
# result = []
#
# for val in numbers:
#     if val >= 0:
#         root = val ** .5
#
#         if root == int(root):
#             result.append(int(root))
#
# print(result)

"""
Задача № 2
"""

# date = '11.09.2001'
# date = date.split('.')
#
# ele = 'Одиннадцать'
#
# result = []
# for val in date:
#     if val == 11:
#         result.append('Одиннадцать')

"""
Задача №3
"""

# import random
#
# result = []
#
# elem = int(input('Введи: '))
#
# for i in range(elem):
#     result.append(random.randint(-100, 100))
#
# print(result)