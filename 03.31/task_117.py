# In this exercise you will create a program that identifies all of the words in a
# string entered by the user. Begin by writing a function that takes a string as
# its only parameter. Your function should return a list of the words in the string
# with the punctuation marks at the edges of the words removed. The punctuation
# marks that you must consider include commas, periods, question marks,
# hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove
# punctuation marks that appear in the middle of a word, such as the apostrophes
# used to form a contraction. For example, if your function is provided with the
# string "Contractions include: don’t, isn’t, and wouldn’t."
# then your function should return the list ["Contractions", "include",
# "don’t", "isn’t", "and", "wouldn’t"].
# Write a main program that demonstrates your function. It should read a string from
# the user and then display all of the words in the string with the punctuation marks
# removed. You will need to import your solution to this exercise when completing
# Exercises 118 and 167. As a result, you should ensure that your main program only
# runs when your file has not been imported into another program.

def get_words(text: str) -> list:
    res = []
    for word in text.split():
        if not word[-1].isalpha():
            res += [word[:-1]]
        else:
            res += [word]
    return res


if __name__ == "__main__":
    print(get_words(input()))


# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-7/task_117.py
# Contractions include: don’t, isn’t, and wouldn’t.
# ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']
#
# Process finished with exit code 0
