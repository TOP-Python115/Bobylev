#!/usr/bin/env python3

# Выведите на экран надпись To be or not to be на разных строках. 
# Пример вывода:
# To be
# or not
# to be

import os

columns, rows = os.get_terminal_size()
text = ["To be", "or not", "to be"]

for string in text:
    print(string.center(columns, ' '))

