# Exercises 75 and 76 previously introduced the notion of a palindrome. Such palindromes
# examined the characters in a string, possibly ignoring spacing and punctuation
# marks, to see if the string was the same forwards and backwards. While
# palindromes are most commonly considered character by character, the notion of
# a palindrome can be extended to larger units. For example, while the sentence “Is
# it crazy how saying sentences backwards creates backwards sentences saying how
# crazy it is?” isn’t a character by character palindrome, it is a palindrome when examined
# a word at a time (and when capitalization and punctuation are ignored). Other
# examples of word by word palindromes include “Herb the sage eats sage, the herb”
# and “Information school graduate seeks graduate school information”.
# Create a program that reads a string from the user. Your program should report
# whether or not the entered string is a word by word palindrome. Ignore spacing and
# punctuation when determining the result.

from task_117 import get_words


def is_word_palindrome(words: list) -> str:
    for i in range(len(words) // 2):
        if not words[i].lower() == words[len(words) - i - 1].lower():
            break
    else:
        return "It is a palindrome"
    return "It is not a palindrome"


assert is_word_palindrome(get_words(
    "Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?")) == "It is a palindrome"
assert is_word_palindrome(get_words("Herb the sage eats sage, the herb")) == "It is a palindrome"
assert is_word_palindrome(
    get_words("Information school graduate seeks graduate school information")) == "It is a palindrome"
assert is_word_palindrome(get_words("aaa bbb ccc ddd eee fff")) == "It is not a palindrome"

print(is_word_palindrome(get_words(input("Введите строку: "))))


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-7/task_118.py
# Введите строку: Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?
# It is a palindrome
#
# Process finished with exit code 0
