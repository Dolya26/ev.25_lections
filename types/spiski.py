# list() -> (список, массив)- изменяемый, последовательный тип данных, который представялет из себя коллекцию каких либо объектов (значений)

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# range() - возвращает последовательность элементов (чисел)

# ls = list(range(1, 101))
# print(ls)
# print(type(ls))

# ls1 = list(range(0, 101, 2))
# # print(ls1)

# ls = list(range(1, 101))
# str1 = 'Hello world!'
# for num in ls:
#     # print(num ** 2 if num %2 == 0 else num ** 3)
#     if num % 2 == 0:
#         print(f'Число {num} четное, квадрат: {num ** 2}')
#     else:
#         print(f'Число {num} нечетное, куб: {num ** 3}')
# -----------------------------------------------------------------------------------

# Методы списков: 

# print(dir([]))

# append(element) - Добавляет element в конец списка 

# ls = [1,2,3]
# print(ls)
# ls.append(5)
# ls.append([6,7,8])
# ls.append(True)
# print(ls)

# extend(iterable) -> расширяет список элементами из iterable object

# ls = [1,2,3]

# ls = [1,2,3]
# ls.append([4,5,6])
# print(ls)
# ls.extend([4,5,6])
# print(ls)

# insert(<index>, <element>) -> добавляет элемент по указонному index

# ls = [1, 2, 3, False]
# ls.insert(1, 4)
# ls.insert(15, True)
# print(ls)

# index(element, [start], [end]) -> возвращает index элемента в списке

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John']
# res = ls.index('name')
# print(res)
# print(ls[res])

# print(ls[0:2])
# print(ls[-1][0])

# count(element) -> возвращает кол-во вхождений element в списке

# ls = [1,2,3,4,5,6,5,5,5]
# result = ls.count(5)
# print(result)

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John', 'North', 'King', 'queen', 'USA']
# print(ls)
# str1 = input('Введите слово: ')
# if str1 in ls:
#     print(f'"{str1}"есть в списке и его индекс: {ls.index(str1)}')
# else:
#     print('Нет!')

# sort() -> сортирует список, если в аргументах передать reverse=True, то список будет отсортирован в убывающем порядке

# import random

# ls= []

# for x in range(0,50):
#     ls.append(random.randint(0, 1000))

# print(ls)
# ls.sort(reverse=True)
# print()
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'Aikol', 'Nurayim', 'makers']
# print(ls)
# print()
# ls.sort(key=len)
# print(ls)

# remove(element) -> удаляет element из списка, если такого нет, то выводится ошибка
# pop([index]) -> удаляет и возвращает элемент по index, но если index не указан, то удаляет последний элемент

# ls = [5,1,2,4,5,5,5]
# # ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)

# ls = [5,1,2,4,5,5,5, 99]
# d = ls.pop(0)
# print(ls)
# print(deleted)
# print(ls.pop())
# print(ls)

# update ---------------------------------
# ls = [1,'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)










