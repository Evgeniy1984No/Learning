"""
Класс Circle
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:

_radius — радиус круга
_diameter — диаметр круга
_area — площадь круга
Класс Circle должен иметь три метода экземпляра:

get_radius() — метод, возвращающий радиус круга
get_diameter() — метод, возвращающий диаметр круга
get_area() — метод, возвращающий площадь круга
Примечание 1. Площадь круга вычисляется по формуле
π
r
2
πr
2
 , где
r
r — радиус круга,
π
π — константа, которая выражает отношение длины окружности к ее диаметру.

Примечание 2. Импортировать константу
π
π можно из модуля math:

from math import pi
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

circle = Circle(1)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
Sample Output 1:

1
2
3
Sample Input 2:

circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
Sample Output 2:

5
10
79
"""
from math import pi


class Circle:
    def __init__(self, r):
        self._radius = r
        self._diameter = 2 * r
        self._area = pi * r ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


