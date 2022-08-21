from task_91 import is_leap_year, get_ordinal_date

assert get_ordinal_date(1, 1, 1) == 1
assert get_ordinal_date(29, 2, 2000) == 60
assert get_ordinal_date(29, 2, 2001) == -1
assert get_ordinal_date(1, 13, 2002) == -1
assert get_ordinal_date(31, 12, 2003) == 365
assert get_ordinal_date(31, 12, 2004) == 366
assert is_leap_year(2000) == True
assert is_leap_year(2001) == False
