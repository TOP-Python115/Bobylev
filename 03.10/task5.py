#!/usr/bin/env python3

# Выведите на экран надпись
# «Life is what happens when you're busy making other plans» John Lennon на разных строках. 
# Пример вывода:
# “Life is what happens
#      when
#          you’re busy making other plans”
#                                  John Lennon.

text = ["\"Life is what happens", "when", "you\'re busy making other plans\""]
tabs = ''
for string in text:
    print(tabs.expandtabs(4), string)
    tabs += '\t'
else:
    print("\t\t\t\tJohn Lennon.")

