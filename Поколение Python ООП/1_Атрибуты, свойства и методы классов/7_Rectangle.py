"""
Класс Rectangle
Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:

length — длина прямоугольника
width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:

perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
Примечание 1. При изменении сторон прямоугольника должны изменяться его периметр и площадь.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
Sample Output 1:

4
5
18
20
Sample Input 2:

rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
Sample Output 2:

2
3
10
6
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length

    perimeter = property(get_perimeter)
    area = property(get_area)


