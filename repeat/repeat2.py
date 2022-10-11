# names = ['Maya Angelou', 'Chimamanda Ngozi Adichie', 'Tobias Wolff', 'Sherman Alexie', 'Jane Austen']
# result = []
# for x in names:
#     x = x.split(' ')
    # print(x)
    # result.append(x[-1])

# result.sort()
# print(result)

# names = []
# for x in range(0, 5):
#     name = input('FIO: ')
#     names.append(name)

# result = []
# for x in names:
#     x = x.split(' ')
#     print(x)
#     result.append(x[-1])

# range(start, stop, [step]) - возвращает последовательность из целых чисел, начиная с start до stop,
# воозвращате итерируемый тип данных range

# x = range(1, 10)
# print(list(x))

# print(x)
# for num in x:
    # print(num)



# res = 0
# for num in range(1, 101):
#     res += num

# print(res)



# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]
# n = 3
# list1 = []
# list2 = []
# list3 = []
# for x in range(0, len(list_), n):
#     list1.append(list_[x])
#     list2.append(list_[x+1])
#     if x + 2 >= len(list_):
#         continue
#     list3.append(list_[x+2])

# res = [list1, list2, list3]
# print(res)



# res = []
# for x in range(0, 3):
#     ls = []
#     for x in range(0, 3):
#         ls.append(0)
#     res.append(ls)
# print(res)


# from itertools import permutations

# res = list(permutations([1,2,3], 3))
# print(res)
