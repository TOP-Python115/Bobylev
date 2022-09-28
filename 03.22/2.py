#!/usr/bin/env python3

# Напишите программу, которая считывает два целых числа m и n (m ≤ n) и выводит в одну строку все числа от m до n включительно.

m, n = int(input()), int(input())

if m <= n:
    for i in range(m, n+1):
        print(i, end=' ')
else:
    print("first number must be less or equal than second")
