# Напишите программу, которая подсчитает количество «счастливых» билетиков в одном рулоне,
# если номер первого билета в рулоне 000001, а номер последнего 999999.

counter = 0
for ticket in range(1, 1000000):
    ticket = str(ticket).rjust(6, '0') # грязный хак с переводом в строку, зато за один проход цикла
    if sum((int(x) for x in ticket[:3])) == sum((int(x) for x in ticket[3:])):
        counter += 1

print(counter)

# Более хорошие решения кажется уже делать с помощью математических формул только.
