# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1, num2)

# print(' hello' * 3) #дублирование строк 

# str1 = '12'
# num1 = 2

# print (str1 + str( num1))


# Инкремент - увеличение значения какой-либо переменной,ПРИМЕР: a - 1 (a +- 1 -> a = a+1 )

# a = 11
# # a += 1
# a = a + 1
# print (a)

# Дикримент - уменьшение значения какой-либо переменной. (a -= 1 -> a - a -1)

# a = 10
# a /= 2
# print (a)

# id() -> номер в ячейке памяти 

# a = 2
# b = 1 
# print (id(a))
# print (id(b))

# type () -> выводит тип заданной переменной

# a = 9
# b = 'hello'
# print (type(a)) 
# print(type(b))

# var = int(input('Введите число')) -> функция стандартного ввода

# примем от пользователя два значения, переводим в тип int и возведем первое число в степень второго числа

# num1 = int (input('введите числo: '))
# num2 = int (input('введите cтепень: '))
# print(num1 ** num2)


# Модуль random - предостовляет функция для генерации случайных чисел, буквы, символы

# import random

# print (dir(random))

# num = random.randint(11111, 99999)
# print(num)

# from random import choice
# import string 

# print(string.ascii_letters)

# a = choice(string.ascii_letters)
# print(a)

# from math import pi 

# r = int (input('введите радиус: '))
# result_P = 2 * r * pi
# result_S = pi * (r**2)
# print ('P ', round(result_P))
# print ('S ', round(result_S))
