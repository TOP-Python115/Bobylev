#!/usr/bin/env python3

# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

nums = map(int, input("Введите 3 числа через пробел: ").split())

result = 0

for num in nums:
    if num > 0:
        result += num

print(result)
