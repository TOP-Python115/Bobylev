# Напишите программу, которая позволит пользователю преобразовывать
# числа из одной системы счисления в другую произвольным образом. Ваша
# программа должна поддерживать все системы счисления в диапазоне от
# 2 до 16 как для входных, так и для выходных данных. Если пользователь
# выберет систему с основанием, выходящим за границы допустимого, на
# экран должна быть выведена ошибка. Разделите код программы на не-
# сколько функций, включая функцию, конвертирующую число из произ-
# вольной системы счисления в десятичную, и обратную функцию, пере-
# водящую значение из десятичной системы в произвольную. В основной
# программе необходимо запросить у пользователя исходную систему счис-
# ления, целевую систему, а также число для преобразования.

def num_to_str(num: int):
    """Конвертирует ввод одного числа в символьное представление"""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    return numbers[num]


def str_to_num(num: str) -> int:
    """Конвертирует ввод одного символа в числовое представление"""
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    try:
        return numbers.index(num.upper())
    except ValueError:
        raise ValueError


def convert(source_system: int, target_system: int, number: str) -> str:
    """Конвертирует из заданной системы счисления в заданную через десятичную"""
    if 2 <= source_system <= 16 or 2 <= target_system <= 16:
        return from_decimal(target_system, to_decimal(source_system, number))
    else:
        return "Диапазон систем счисления от 2 до 16"


def get_number(number: list) -> str:
    """Преобразует список чисел в символы"""
    res = ''
    for num in number:
        res += str(num_to_str(num))
    return res


def from_decimal(target_system: int, number: int) -> str:
    """Конвертирует из десятичной системы счисления в заданную"""
    res = []
    while number >= target_system:
        res.append(number % target_system)
        number = number // target_system
    else:
        res.append(number)
    return get_number(res[::-1])


def to_decimal(source_system: int, number: str) -> int:
    """Конвертирует из заданной системы счисления в десятичную"""
    res = []
    numbers = []
    for n in number:
        numbers.insert(0, str_to_num(n))
    for n in range(len(numbers), 0, -1):
        res.append(numbers[n - 1] * (source_system ** (n - 1)))
    return sum(res)


print(convert(16, 10, 'ABC'))
