# Разработайте функцию, принимающую в качестве единственного па-
# раметра порядковую дату, включающую в себя год и день по порядку.
# В качестве результата функция должна возвращать день и месяц, соот-
# ветствующие переданной порядковой дате. Убедитесь, что ваша функция
# корректно обрабатывает високосные годы.
# Используйте эту функцию, а также функцию ordinalDate, написанную
# при выполнении упражнения 91, для разработки основной программы.
# Для начала должен производиться запрос порядковой даты у пользова-
# теля. После этого программа должна вычислить вторую дату, отстоящую
# от первой на определенное количество дней. Например, ваша программа
# могла бы запрашивать у пользователя порядковую дату, когда был при-
# обретен товар, и выводить последнюю дату, когда можно осуществить
# возврат (согласно определенным правилам возврата товаров). Или вы
# могли бы спрогнозировать дату появления ребенка на свет на основании
# срока беременности в 280 дней. Удостоверьтесь, что программа корректно
# обрабатывает ситуации, когда заданная дата и расчетная находятся
# в разных годах.


def is_leap_year(year: int) -> bool:
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False


def get_days_of_year(year: int) -> tuple:
    return (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) if is_leap_year(year) \
        else (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def get_ordinal_date(day: int, month: int, year: int) -> int:
    if day < 1 or day > 31 or month < 1 or month > 12:
        return -1
    if not is_leap_year(year) and month == 2 and day >= 29:
        return -1
    return sum(get_days_of_year(year)[:month - 1]) + day


def get_date(year: int, day: int) -> tuple[int, int]:
    if day < 1:
        return -1, -1
    for i in range(12):
        if day <= sum(get_days_of_year(year)[:i + 1]):
            return day - sum(get_days_of_year(year)[:i]), i + 1
    return -1, -1


if __name__ == "__main__":
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))
    warranty_days = int(input("Введите количество дней гарантии: "))
    days = get_ordinal_date(day, month, year) + warranty_days
    while days > sum(get_days_of_year(year)):
        days -= sum(get_days_of_year(year))
        year += 1
    day, month = get_date(year, days)

    print(day, month, year)
