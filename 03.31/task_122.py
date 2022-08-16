# Pig Latin is a language constructed by transforming English words. While the origins
# of the language are unknown, it is mentioned in at least two documents from
# the nineteenth century, suggesting that it has existed for more than 100 years. The
# following rules are used to translate English into Pig Latin:
# • If theword begins with a consonant (including y), then all letters at the beginning of
# theword, up to the first vowel (excluding y), are removed and then added to the end
# of the word, followed by ay. For example, computer becomes omputercay
# and think becomes inkthay.
# • If the word begins with a vowel (not including y), then way is added to the end
# of the word. For example, algorithm becomes algorithmway and office
# becomes officeway.
# Write a program that reads a line of text from the user. Then your program should
# translate the line into Pig Latin and display the result. You may assume that the string
# entered by the user only contains lowercase letters and spaces.

def get_pig_latin(text: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u')
    res = text
    if text[0] in vowels:
        return text + "way"
    for letter in text:
        if letter not in vowels:
            res = res[1:] + res[0]
        else:
            break
    return res + "ay"

# Тесты:
assert get_pig_latin("computer") == "omputercay"
assert get_pig_latin("think") == "inkthay"
assert get_pig_latin("algorithm") == "algorithmway"
assert get_pig_latin("office") == "officeway"

text = input("Введите текст: ").split()
for word in text:
    print(get_pig_latin(word), end=' ')

# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-7/task_122.py
# Введите текст: computer think algorithm office
# omputercay inkthay algorithmway officeway
# Process finished with exit code 0
