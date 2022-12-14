# Многие в своих сообщениях не ставят заглавные буквы, особенно если ис-
# пользуют для набора мобильные устройства. Создайте функцию, которая
# будет принимать на вход исходную строку и возвращать строку с восста-
# новленными заглавными буквами. По существу, ваша функция должна:
# - сделать заглавной первую букву в строке, не считая пробелы;
# - сделать заглавной первую букву после точки, восклицательного или
# вопросительного знака, не считая пробелы;
# - если текст на английском языке, сделать заглавными буквы «i», ко-
# торым предшествует пробел или за которыми следует пробел, точка,
# восклицательный или вопросительный знак.
# Реализация такого рода автоматической корректуры исключит боль-
# шую часть ошибок с регистром букв. Например, строку «what time do i have
# to be there? what’s the address? this time i’ll try to be on time!» ваша функция
# должна преобразовать в более приемлемый вариант «What time do I have
# to be there? What’s the address? This time I’ll try to be on time!». В основной
# программе запросите у пользователя исходную строку, обработайте ее
# при помощи своей функции и выведите на экран итоговый результат.


def capitalize(text: str) -> str:
    res = text.split()
    punctuation = ".!?"
    for i in range(len(res)):
        if i == 0:
            res[i] = res[i].capitalize()
        if res[i] == 'i':
            res[i] = res[i].capitalize()
        if "’" or "'" in res[i] and 'i' in res[i]:
            if res[i][res[i].find('i') + 1] in "'’":
                res[i] = res[i].capitalize()
        if i > 0 and res[i - 1][-1] in punctuation:
            res[i] = res[i].capitalize()
    return ' '.join(res)


if __name__ == "__main__":
    print(capitalize(input("Введите строку: ")))
