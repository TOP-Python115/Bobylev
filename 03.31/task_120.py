# When writing out a list of items in English, one normally separates the items with
# commas. In addition, theword “and” is normally included before the last item, unless
# the list only contains one item. Consider the following four lists:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function
# should return a string that contains all of the items in the list, formatted in the manner
# described previously, as its only result. While the examples shown previously only
# include lists containing four elements or less, your function should behave correctly
# for lists of any length. Include a main program that reads several items from the user,
# formats them by calling your function, and then displays the result returned by the
# function.

def get_styled(items: list) -> str:
    res = ''
    if len(items) <= 1:
        return items[0]
    for i in range(len(items) - 2):
        res += f"{items[i]}, "
    return res + f"{items[-2]} and {items[-1]}"


words = []

while word := input("Введите слово: "):
    words += [word]

print(get_styled(words))


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-7/task_120.py
# Введите слово: apples
# Введите слово: oranges
# Введите слово: bananas
# Введите слово: lemons
# Введите слово:
# apples, oranges, bananas and lemons
#
# Process finished with exit code 0
