# Вам дана иерархия наследования, проблема которой заключается в необходимости реализации огромного количества классов.
# Необходимо провести рефакторинг этой иерархии, задав в базовом классе Shape конструктор, принимающий интерфейса Renderer, объявленный как:

#   class Renderer(ABC):
#       @property
#       def what_to_render_as(self):
#           return None

# VectorRenderer и RasterRenderer так же должны оперировать через интерфейс Renderer.
# Каждый наследник класса Shape должен иметь конструктор, принимающий Renderer и реализованный таким образом, что вызовы __str__() на экземплярах этих наследников должны работать корректно.
# Например:
#   str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"

# Sample Input:
#   1
# Sample Output:
#   Drawing Square as lines Drawing Triangle as pixels

import sys
from abc import ABC


# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


# код для проверки
sq = Square(VectorRenderer())
tr = Triangle(RasterRenderer())

print(f'{str(sq)} {str(tr)}')
