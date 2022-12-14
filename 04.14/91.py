# Порядковая дата содержит номер года и порядковый номер дня в этом
# году – оба в целочисленном формате. При этом год может быть любым
# согласно григорианскому календарю, а номер дня – числом в интервале
# от 1 до 366 (чтобы учесть високосные годы). Порядковые даты удобно
# использовать при расчете разницы в днях, когда счет ведется именно
# в днях, а не месяцах. Например, это может касаться 90-дневного периода
# возврата товара для покупателей, расчета срока годности товаров или
# прогнозируемой даты появления малыша на свет.
# Напишите функцию с именем ordinalDate, принимающую на вход три
# целых числа: день, месяц и год. Функция должна возвращать порядковый
# номер заданного дня в указанном году. В основной программе у пользо-
# вателя должны запрашиваться день, месяц и год соответственно и выво-
# диться на экран порядковый номер дня в заданном году. Программа долж-
# на запускаться только в том случае, если она не импортирована в виде
# модуля в другой файл.

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


if __name__ == '__main__':
    print(get_ordinal_date(int(input("day: ")), int(input("month: ")), int(input("year: "))))
