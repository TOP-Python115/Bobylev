# While the popularity of cheques as a payment method has diminished in recent years,
# some companies still issue them to pay employees or vendors. The amount being
# paid normally appears on a cheque twice, with one occurrence written using digits,
# and the other occurrence written using English words. Repeating the amount in two
# different formsmakes it much more difficult for an unscrupulous employee or vendor
# to modify the amount on the cheque before depositing it.
# In this exercise, your task is to create a function that takes an integer between 0 and
# 999 as its only parameter, and returns a string containing the English words for that
# number. For example, if the parameter to the function is 142 then your function should
# return “one hundred forty two”. Use one or more dictionaries to implement
# your solution rather than large if/elif/else constructs. Include a main program that
# reads an integer from the user and displays its value in English words.

numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

n = int(input("Введите число: "))
res = []
if n > 999 or n < 0:
    res = ["Необходимо число от 0 до 999"]
elif n == 0:
    res = [numbers[n]]
else:
    if 100 <= n < 200:
        res += [numbers[n // 100], "hundred"]
    elif n >= 200:
        res += [numbers[n // 100], "hundreds"]
    if n > 100 and n % 100 < 10:
        res += ["and"]
    n = n % 100
    if 0 < n < 20:
        res += [numbers[n]]
    else:
        if n % 10:
            res += [tens[n - n % 10], numbers[n % 10]]
        elif n > 0:
            res += [tens[n]]
print(*res)
