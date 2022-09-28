#!/usr/bin/env python3

# Пользователь вводит с клавиатуры три числа.
# Первое число — зарплата за месяц, 
# второе число — сумма месячного платежа по кредиту в банке,
# третье число — задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат.

salary = int(input("Enter your salary: "))
mortgage = int(input("Enter your monthly mortgage payment: "))
bills = int(input("Enter your monthly bills: "))

print(f"you will have {salary - mortgage - bills} coins left")
