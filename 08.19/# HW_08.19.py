# Магический квадрат - матрица чисел, в которой сумма чисел любой строки, столбца или диагонали одинакова. Вам даётся проект из трёх классов, которые могут быть использованы для построения магического квадрата.

# Это классы:
#   Generator: этот класс генерирует список из девяти случайных чисел
#   Splitter: это класс, который принимает двумерный список и разбивает его на все возможные одномерные списки. Он даёт в результате колонки, строки и две диагонали.
#   Verifier: этот класс принимает двумерный список и проверяет, что сумма чисел любого из содержимых списков одинакова.

# Вам только остаётся реализовать фасад, названный MagicSquareGenerator который генерирует магический квадрат заданного размера.

from random import randint


class Generator:
    @staticmethod
    def generate(count: int):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    @staticmethod
    def split(array) -> list:
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    @staticmethod
    def verify(arrays) -> bool:
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    # СДЕЛАТЬ: реализовать простой интерфейс для сборки и проверки магического квадрата
    def __init__(self, size: int):
        self.size = size
        self.rows = self._generate()
        self.__max_wd = max(max(len(str(el)) for el in row) for row in self.rows) + 1

    def _generate(self):
        while True:
            rows = []
            for _ in range(self.size):
                rows += [Generator().generate(self.size)]
            item = Splitter().split(rows)
            if Verifier().verify(item):
                return rows

    def __str__(self):
        ret = ''
        for row in self.rows:
            ret += ''.join(f'{el:>{self.__max_wd}}' for el in row) + '\n'
        return ret[:-1]


ms = MagicSquareGenerator(3)
print(ms)

# 2 3 4
# 5 3 1
# 2 3 4
