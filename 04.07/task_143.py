# Two words are anagrams if they contain all of the same letters, but in a different
# order. For example, “evil” and “live” are anagrams because each contains one “e”,
# one “i”, one “l”, and one “v”. Create a program that reads two strings from the user,
# determines whether or not they are anagrams, and reports the result.

string_1 = input("Введите первое слово: ")
string_2 = input("Введите второе слово: ")

print("anagrams" if {k: string_1.count(k) for k in string_1} == {k: string_2.count(k) for k in string_2} else "not anagrams")


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-9/task_143.py
# Введите первое слово: evil
# Введите второе слово: live
# anagrams
#
# Process finished with exit code 0
# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-9/task_143.py
# Введите первое слово: elvis
# Введите второе слово: vised
# not anagrams
#
# Process finished with exit code 0
