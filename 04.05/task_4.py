# На вход программе подается строка, содержащая имена файлов, разделенные символом пробела.
# Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов.
# Для этого необходимо прибавлять к повторяющимся именам постфикс "_n", где n – количество раз, сколько такой идентификатор уже встречался.
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.
#
# Пример ввода:
# 	1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp
#
# Пример вывода:
# 	1.py 1_2.py aux.h main.cpp functions.h main_2.cpp 2.py main_3.cpp

files_list = input("Список файлов: ").split()
counter = {}
result = []


def rename(name: str, number: int) -> str:
    return f"{name[:name.rindex('.')]}_{number}{name[name.rindex('.'):]}"


for item in files_list:
    counter[item] = files_list.count(item)

files_list.reverse()

for item in files_list:
    if counter[item] > 1:
        result += [rename(item, counter[item])]
        counter[item] -= 1
    else:
        result += [item]

result.reverse()
print(*result)
