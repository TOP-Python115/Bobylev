# Exercise 114: Negatives,Zeros and Positives
#
# Create a program that reads integers from the user until a blank line is entered. Once
# all of the integers have been read your program should display all of the negative
# numbers, followed by all of the zeros, followed by all of the positive numbers.Within
# each group the numbers should be displayed in the same order that they were entered
# by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
# your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
# should display each value on its own line.

data = []
while number := input("Введите число: "):
    data += [int(number)]

print(*[x for x in data if x < 0], sep='\n')
print(*[x for x in data if x == 0], sep='\n')
print(*[x for x in data if x > 0], sep='\n')
