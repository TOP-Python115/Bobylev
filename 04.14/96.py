# Упражнение 96. Является ли строка целым числом?
# (Решено. 30 строк)
# В данном упражнении вам предстоит написать функцию с именем isInteger,
# определяющую, представляет ли введенная строка целочисленное
# значение. При проверке вы можете игнорировать ведущие и замыкаю-
# щие пробелы в строке. После исключения лишних пробелов строку можно
# считать представляющей целое число, если ее длина больше или равна
# одному символу и она целиком состоит из цифр. Возможен также вариант
# с ведущим знаком «+» или «-», после которого должны идти цифры.
# В основной программе у пользователя должна запрашиваться исходная
# строка и выводиться сообщение о том, можно ли введенное значение вос-
# принимать как целое число. Убедитесь, что основная программа не будет
# запускаться, если файл импортирован в другой файл в качестве модуля.

def isInteger(value: str) -> bool:
    numbers = '0123456789'
    signs = '+-'
    string = value.strip()
    if len(string) == 1 and string in numbers:
        return True
    if string[0] in signs or string[0] in numbers:
        for symbol in string[1:]:
            if symbol not in numbers:
                return False
    else:
        return False
    return True


if __name__ == '__main__':
    while number := input():
        print(isInteger(number))

