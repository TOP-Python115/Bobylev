#!/usr/bin/env python3

# Напишите программу, которая определяет, является число чётным или нечётным.
isOdd = int(input("Введите число ")) % 2
print( "Нечетное" if isOdd else "Четное" )
