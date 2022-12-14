# Exercise 119: Below and Above Average

# Write a program that reads numbers from the user until a blank line is entered. Your
# program should display the average of all of the values entered by the user. Then
# the program should display all of the below average values, followed by all of the
# average values (if any), followed by all of the above average values. An appropriate
# label should be displayed before each list of values.

def avg(l: list) -> float:
    return sum(l) / len(l)


data = []
while number := input("Введите число: "):
    data += [int(number)]

print("Ниже среднего: ", *[x for x in data if x < avg(data)])
print("Среднее: ", *[x for x in data if x == avg(data)])
print("Выше среднего: ", *[x for x in data if x > avg(data)])
