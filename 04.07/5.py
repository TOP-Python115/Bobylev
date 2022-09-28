# Напишите программу, объединяющую словари из списка в один общий.
#
# Программа должна принимать список словарей (сгенерируйте на generatedata.com).
# Итоговый словарь:
# 	каждый ключ содержит множество уникальных значений соответствовавших аналогичным ключам в исходных словарях
from pprint import pprint

# Вообще не понимаю как можно решить это задание с помощью представления словарей
# На каждой итерации мне нужно добавлять значение в множество,
# но это не возможно сделать если использовать представление
# Поэтому отправляю вариант с циклами.

data = [
    {
        'list': "1",
        'name': "Constance Burks",
        'phone': "(544) 836-5632",
        'date': "Jun 30, 2021",
        'company': "Sem Molestie Sodales Ltd"
    },
    {
        'list': "3",
        'name': "Eaton Holden",
        'phone': "1-648-221-0750",
        'date': "Mar 4, 2022",
        'company': "Turpis In Corp."
    },
    {
        'list': "19",
        'name': "Remedios Ball",
        'phone': "1-176-188-1782",
        'date': "Apr 10, 2022",
        'company': "A Magna PC"
    },
    {
        'list': "17",
        'name': "Kylee Meadows",
        'phone': "(624) 423-7064",
        'date': "May 8, 2023",
        'company': "Donec Consulting"
    },
    {
        'list': "9",
        'name': "Erica Baird",
        'phone': "1-168-535-1220",
        'date': "Apr 30, 2022",
        'company': "Eu Accumsan Limited"
    },
    {
        'list': "9",
        'name': "Tallulah Potts",
        'phone': "(322) 358-1458",
        'date': "Mar 30, 2022",
        'company': "Arcu Iaculis Corp."
    },
    {
        'list': "1",
        'name': "Isaac Herman",
        'phone': "(609) 963-4618",
        'date': "May 15, 2023",
        'company': "Sed Dui Fusce Company"
    },
    {
        'list': "5",
        'name': "Shad O'Neill",
        'phone': "1-968-419-1284",
        'date': "Aug 13, 2022",
        'company': "Risus At Fringilla Incorporated"
    },
    {
        'list': "7",
        'name': "Brody Robinson",
        'phone': "(583) 286-1176",
        'date': "Aug 15, 2022",
        'company': "Curae Industries"
    },
    {
        'list': "11",
        'name': "Kaitlin Duke",
        'phone': "(282) 944-9495",
        'date': "Dec 18, 2022",
        'company': "Aliquet Phasellus LLP"
    },
    {
        'list': "7",
        'name': "Steel Puckett",
        'phone': "(862) 781-5693",
        'date': "Aug 12, 2022",
        'company': "Diam Sed Ltd"
    },
    {
        'list': "7",
        'name': "Amos Murphy",
        'phone': "(237) 156-5964",
        'date': "Nov 7, 2022",
        'company': "At Fringilla LLC"
    },
    {
        'list': "17",
        'name': "Norman Henderson",
        'phone': "(728) 425-2318",
        'date': "Nov 15, 2021",
        'company': "Nulla Corporation"
    },
    {
        'list': "19",
        'name': "Angelica Bean",
        'phone': "(533) 652-6668",
        'date': "Jan 7, 2023",
        'company': "Inceptos Hymenaeos Ltd"
    },
    {
        'list': "1",
        'name': "Matthew Beasley",
        'phone': "(451) 280-1090",
        'date': "Jun 25, 2021",
        'company': "Quis Diam LLP"
    },
    {
        'list': "5",
        'name': "Kyle Boyer",
        'phone': "1-458-818-3673",
        'date': "Jul 10, 2022",
        'company': "Malesuada Vel Industries"
    },
    {
        'list': "1",
        'name': "Nadine Booker",
        'phone': "(801) 832-5637",
        'date': "Dec 31, 2021",
        'company': "Ut Cursus Company"
    },
    {
        'list': "19",
        'name': "Lewis Gutierrez",
        'phone': "1-626-328-7464",
        'date': "Dec 25, 2022",
        'company': "Metus Urna Consulting"
    },
    {
        'list': "13",
        'name': "Wayne Clemons",
        'phone': "1-352-588-8904",
        'date': "Apr 7, 2022",
        'company': "Nullam Feugiat Corporation"
    },
    {
        'list': "9",
        'name': "Adrienne Patterson",
        'phone': "(271) 582-4411",
        'date': "Mar 8, 2022",
        'company': "Id Ante Ltd"
    }
]
res = {key: {v for item in data for k, v in item.items() if k == key} for item in data for key in item.keys()}
pprint(res)
