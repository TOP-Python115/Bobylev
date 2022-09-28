#!/usr/bin/env python3

# Вводятся два целых числа не равных нулю.
# Напишите программу, которая проверяет делится ли первое число на второе нацело.
# Программа выводит сообщение об этом, а также частное и остаток, если он есть.
# Для вывода используйте f-строку.

a, b = map(int, input("Введите 2 числа через пробел: ").split()) 

if a % b: 
    print(f"{a} не делится на {b} нацело\n",
          f"Частное: {a//b}\n",
          f"Остаток: {a%b}")
else:
    print(f"{a} делится на {b} нацело\n",
          f"Частное: {a/b}")
