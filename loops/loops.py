# Циклы - это конструкция, при помощи которых можно органивать многократное исполнение определённого кода

# while <exception == True>:
    # <body>
# <else>
    # <body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз!')
#     i += 1
# else:
#     print('Конец цикла!')

# print('Начало кода')

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Введите имя: ')
#     name2 = input('Введите второе имя: ')
#     i += 1
#     if i > 4:
#         print('Цикл остановлен!')
#         break
# else:
#     print('Вы ввели правильное имя!')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None

# while username != admin[0] or password != admin[1]:
#     username = input('login: ')
#     password = input('password: ')
#     i -= 1
#     if i == 0:
#         print('Vacban na 5 minut!')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno voshli v sistemu!')

# -----------------------------------------------

# for <variable> in <iterable object>:
    # <body>

# list_ = [0,1,2,3,4,5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# for x in list_:
#     print(x)

# ---------------------------------------------------
# ls = [1,2,3,4,5,6,7,8,9,0]
# for x in ls:
    # print(f'Element: {x}')
# ======
# ls = [1,2,3,4,5,6,7,8,9,0]
# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}')
#     i += 1

# --------------------------------------------------------

# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('Vvedite secret cod: ')

# while word not in secret_list:
#     print('Incorect word! Try one more time!')
#     word = input('Vvedite secret cod: ')

# print(f'Welcome my friend, {word}!')

# 1)
# steps = 8
# path = 'UDDDUDUU'
# dolina = 0
# sea_level = 0
# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == 'D':
#         sea_level -= 1

# print(dolina)



# 2)
# steps = 9
# path = 'UDDUUDDUU'
# dolina = 0
# sea_level = 0
# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == 'D':
#         sea_level -= 1

# print(dolina)


