# Create a program that determines and displays the number of unique characters in a
# string entered by the user. For example, Hello, World! has 10 unique characters
# while zzz has only one unique character. Use a dictionary or set to solve this problem.

# Вариант со словарём
print(len({key: '' for key in input("Введите строку: ")}.keys()))

# Вариант с множеством
# print(len(set(input("Введите строку: "))))


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-9/task_142.py
# Введите строку: Hello, World!
# 10
#
# Process finished with exit code 0
