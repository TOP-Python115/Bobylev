# The notion of anagrams can be extended to multiple words. For example, “William
# Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
# spacing are ignored.
# Extend your program from Exercise 143 so that it is able to check if two phrases
# are anagrams. Your program should ignore capitalization, punctuation marks and
# spacing when making the determination.

string_1 = input("Введите первую строку: ").lower()
string_2 = input("Введите вторую строку: ").lower()

# Получился адский однострочник :D
# print("anagrams" if {k: string_1.count(k) for k in string_1 if k.isalpha()} == {k: string_2.count(k) for k in string_2 if k.isalpha()} else "not anagrams")

# Вот так получше читается
d1 = {k: string_1.count(k) for k in string_1 if k.isalpha()}
d2 = {k: string_2.count(k) for k in string_2 if k.isalpha()}

print("anagrams" if d1 == d2 else "not anagrams")


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-9/task_144.py
# Введите первую строку: William Shakespeare!
# Введите вторую строку: I am, a weakish speller?
# anagrams
#
# Process finished with exit code 0
# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-9/task_144.py
# Введите первую строку: aaa ddd fff !!!!
# Введите вторую строку: aaaa dd fff !!!!
# not anagrams
#
# Process finished with exit code 0
