#!/usr/bin/env python3

# Пользователь вводит с клавиатуры три числа.
# Необхо-димо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.

numbers = input("Введите 3 числа через пробел: ").split()

summ = 0
multipl = 1

for num in numbers:
    summ += int(num)
    multipl *= int(num)

print(f"Сумма: {summ}\nПроизведение: {multipl}")
