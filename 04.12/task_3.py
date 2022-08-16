# Составьте программу для регистронезависимого частотного анализа букв в тексте
# в зависимости от длины слова, в котором встречается буква
#
# Необходимо составить словарь, ключами в котором будут строки с буквами.
# Значениями будут вложенные словари с ключами в виде чисел – длин слов, в которых встречается эта буква;
# значениями вложенных словарей должна быть частота.
#
# Пример:
#     {..., 'ф': {4: 6, 5: 6, 6: 38, 7: 10, 8: 1, 9: 1}, ...}

# В оригинальном тексте есть одна буква 'p' в латинице, не путать с 'р' в кириллице

from text import text
from pprint import pprint

words = [x.strip("…»«.,\"';!?") for x in text.lower().split()]
res = {k: {} for k in text.lower() if k.isalpha()}
# res = {'а': {}}

# print(sorted(res))
for letter in res.keys():
    for word in words:
        if letter in word:
            if len(word) in res[letter].keys():
                res[letter][len(word)] += 1
            else:
                res[letter][len(word)] = 1

pprint(res)
