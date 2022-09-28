#!/usr/bin/env python3

# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
# Последовательность Фибоначчи – это последовательность натуральных чисел, которая начинается с двух единиц, а каждое последующие число является суммой двух предыдущих: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

n = int(input())
result = ''

# There is nothing to calculate in first two cases
if n <= 1:
    result += '1 '
else:
    result += '1 1 '
# In other cases there is for loop in which I save previous two numbers and calculate next one.
if n > 2:
    a,b,c = 1,1,0
    for _ in range(3, n+1):
        c = a + b
        a = b
        b = c
        result += f'{c} '

print(result)
