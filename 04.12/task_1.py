# Даны два списка, содержащие целые числа.
# Необходимо написать программу, которая удаляет из обоих списков
# пересекающиеся элементы – то есть элементы, представленные в обоих списках
#
# Подсказка: заполните входные списки используя представления списков и функцию randrange() из модуля random

from random import randrange

list_1 = [randrange(0, 10, 1) for _ in range(10)]
list_2 = [randrange(0, 10, 1) for _ in range(10)]

print(sorted(list_1))
print(sorted(list_2))

for elem in set(list_1).intersection(list_2):
    while elem in list_1:
        list_1.remove(elem)
    while elem in list_2:
        list_2.remove(elem)

print("----")
print(sorted(list_1))
print(sorted(list_2))


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-10/task_1.py
# [1, 1, 3, 4, 4, 5, 7, 7, 8, 9]
# [0, 0, 2, 3, 3, 6, 8, 8, 9, 9]
# ----
# [1, 1, 4, 4, 5, 7, 7]
# [0, 0, 2, 6]
