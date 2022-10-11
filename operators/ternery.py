# sentence = input('Введите предложение: ')

# if sentence[-1] == '?':
#     print('Предложение вопросительное')
# else:
#     print('Обычное предложение')

# sentence = input('Введите предложение: ')
# print('Предложение вопросительное' if sentence [-1] == '?' else 'Обычное предложение')
# ----------------------------------------------------------------------------------------------------------
# Ternery operator(Тернарный оператор) - конструкция, которая аналогична по своим свойствам и действию конструкцию if/else, то при этом 
# записывается в одну строчку кода.
# <выражение если в условии True> ig <условие> else <выражение если False>

# number = 15
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)

# from string import digits

# symbols = digits + '-'
# print(symbols)
# number = input('Введите число: ')
# is_correct = True
# for i in number:
#     if i not in symbols:
#         is_correct = False 

# if is_correct:
#     print('Yes number!')
#     number = int(number)
#     print('Your number:', number)
#     result = number if number >= 0 else -number
#     print(result)
# else: 
#     print('Invalid values!')

# -----------------------------------------------------------------------------------------------------
# if number.isdigit():
#     number = int(number)
#     print('Да число!')
# else:
#     print('Вы ввели не число! ')
# -----------------------------------------------------------------------------------------------------
# import string #string.digits

from string import digits

flag = True
symbols = digits + '-' + '.'

while flag:
    is_correct_number = True
    num1 = input('Введите первое число: ')

    if len(num1) <=1 and (num1 == '.' or num1 == '-') or not num1:
            print('Вы ввели неправильное число!')
            is_correct_number = False 
    for x in num1:
        if x not in symbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break
            
            
    num2 = input('Введите второе число: ')
    if len(num2) <=1 and (num2 == '.' or num2 == '-') or not num2:
            print('Вы ввели неправильное число!')
            is_correct_number = False 
    for x in num2:
        if x not in symbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break 
    if not is_correct_number:
        continue

    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    operator = input('Введите опертатор(+, -, *, /): ')
    if operator == '+': 
        print(f'Результат: {num1 + num2}')
    elif operator == '-':
        print(f'Результат: {num1 - num2}')
    elif operator == '*':
        print(f'Результат: {num1 * num2}')
    elif operator == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'Результат: {num1 / num2}')
    else:
        print('Вы ввели неправильный оператор!')

    choice = input('Хотите остановаить?(yes): ')
    if choice.lower() == 'yes':
        flag = False
        print('Пока!')

