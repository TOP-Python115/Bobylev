# Extend your solution to Exercise 122 so that it correctly handles uppercase letters and
# punctuation marks such as commas, periods, question marks and exclamation marks.
# If an English word begins with an uppercase letter then its Pig Latin representation
# should also begin with an uppercase letter and the uppercase letter moved to the end of
# the word should be changed to lowercase. For example, Computer should become
# Omputercay. If a word ends in a punctuation mark then the punctuation mark
# should remain at the end of the word after the transformation has been performed.
# For example, Science! should become Iencescay!.


def get_pig_latin(text: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    res = text

    # Сохранить последний символ если это не буква и убираю его из результата
    last = '' if text[-1].isalpha() else text[-1]
    if last:
        res = text[:-1]

    # Если начинается с гласной, то просто формирую строку
    if text[0] in vowels:
        return res + "way" + last

    # Если начинается с согласной, то сначала проверяю является ли первая буква заглавной
    if text[0].isupper():
        # Если является, то при перестановке букв учитываю это
        for letter in text:
            if letter not in vowels:
                res = res[1].upper() + res[2:] + res[0].lower()
            else:
                break
    else:
        # Если нет, то просто переставляю буквы
        for letter in text:
            if letter not in vowels:
                res = res[1:] + res[0]
            else:
                break
    # В конечном результате добавляю сохранённый ранее знак препинания, или пустоту
    return res + "ay" + last

# Тесты:
assert get_pig_latin("Computer") == "Omputercay"
assert get_pig_latin("Algorithm") == "Algorithmway"
assert get_pig_latin("algorithm!") == "algorithmway!"
assert get_pig_latin("Science!") == "Iencescay!"
assert get_pig_latin("computer") == "omputercay"
assert get_pig_latin("think") == "inkthay"
assert get_pig_latin("algorithm") == "algorithmway"
assert get_pig_latin("office") == "officeway"


text = input("Введите текст: ").split()
for word in text:
    print(get_pig_latin(word), end=' ')

# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-7/task_123.py
# Введите текст: Computer Algorithm algorithm! Science! computer think algorithm office
# Omputercay Algorithmway algorithmway! Iencescay! omputercay inkthay algorithmway officeway
# Process finished with exit code 0
