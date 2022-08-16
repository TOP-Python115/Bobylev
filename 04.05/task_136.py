# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value to
# search for as its only parameters. It will return a (possibly empty) list of keys from
# the dictionary that map to the provided value.
# Include amain program that demonstrates the reverseLookup function as part
# of your solution to this exercise. Your program should create a dictionary and then
# show that the reverseLookup function works correctly when it returns multiple
# keys, a single key, and no keys. Ensure that your main program only runs when
# the file containing your solution to this exercise has not been imported into another
# program.

d = {"name": "Hakeem Warren",
     "phone": "1-794-278-7557",
     "email": "dolor@hotmail.ca",
     "date": "Apr 24, 2023",
     "time": "5:06 AM",
     "company": "Urna Industries",
     "address": "4275 Vulputate Avenue",
     "city": "Anand",
     "postalZip": "1842 GY",
     "region": "North Island",
     "country": "Russian Federation"
     }


while search := input("Слово для поиска: "):
    res = []
    for key in d:
        if search in key:
            res += [key]
    print(res)


