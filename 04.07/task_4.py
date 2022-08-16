# На вход программе подается строка текста.
#
# Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Регистр игнорировать, знаки препинания игнорировать.

text = input("Введите строку: ").lower().split()

# Формирую список слов с удалением знаков пунктуации
words = [w.strip(".,\"'!?") for w in text]
# Считаю количество повторений
counters = {w: words.count(w) for w in words}
# Сначала сортирую по количеству повторений
s1 = dict(sorted(counters.items(), key=lambda item: item[1]))
# Потом сортирую по ключам словаря и вывожу самый первый ключ
print(sorted(s1.keys())[0])

# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-9/task_4.py
# Введите строку: aaa, bbb, aaa, bbb, aaa, ccc, aa, a,
# a
#
# Process finished with exit code 0
