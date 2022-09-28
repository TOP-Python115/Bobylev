# Напишите функцию, которая вычисляет набор средних значений для итерируемого объекта.
# Функция принимает на вход один аргумент, который может быть итерируемым объектом str, list или tuple.
#     В случае, если функции передаётся на вход строка, то она должна содержать только целые или вещественные числа, разделённые пробелом
#     В случае, если функции передан объект другого типа или аргумент содержит что-то помимо целых или вещественных чисел, то функция должна вернуть None
# Функция должна вычислить среднее арифметическое, геометрическое, квадратичное и гармоническое
#     https://mateshka.ru/math/arithmetic/srednie-velichini.html
# Четыре значения должны быть упакованы в словарь с ключами-подписями. Порядок расположения элементов в словаре должен следовать возрастанию величины средних значений.
# В случае корректного вычисления средних, функция должна вернуть итоговый словарь
# Протестировать со случайными вещественными числами: используйте функции модуля random или заранее сгенерированные данные (generatedata.com)

from random import randrange as rr

def get_average(numbers):
    result = {}
    if not isinstance(numbers, (str, tuple, list)):
        return None
    if isinstance(numbers, str):
        values = numbers.split()
    else:
        values = numbers
    try:
        values = tuple(map(float, values))
    except ValueError:
        return None
    geometric = 1
    rms = 0
    harmonic = 0
    for value in values:
        geometric *= value
        rms += value * value
        try:
            harmonic += 1 / value
        except ZeroDivisionError:
            # По условию задачи не понятно, падать в таком случае, возвращать None или ещё что-то.
            # Решил использовать очень маленькое число
            harmonic += 1 / 0.1e-200
    result['arithmetic'] = sum(values) / len(values)
    result['geometric'] = geometric ** (1 / len(values))
    result['rms'] = ((1 / len(values)) * rms) ** 0.5
    result['harmonic'] = len(values) / harmonic

    return {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}


print(get_average([rr(0, 100) for _ in range(100)]))
print(get_average([rr(1, 100) for _ in range(100)]))



# /usr/local/bin/python3.9 /Users/a.bobylev/itstep/DZ/python/dz-11/task_5.py
# {'geometric': 0.0, 'harmonic': 5e-200, 'arithmetic': 48.13, 'rms': 57.143066071046626}
# {'harmonic': 14.509044439653115, 'geometric': 30.819518534328534, 'arithmetic': 43.08, 'rms': 50.90049115676587}
