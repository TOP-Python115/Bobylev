#!/usr/bin/env python3

# На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

n = int(input())

res = 0

for i in range(1, n+1):
    if not n % i:
        res += i
print(res)
