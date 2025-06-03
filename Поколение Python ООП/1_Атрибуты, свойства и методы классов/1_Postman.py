"""
Класс Postman
Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Postman должен иметь один атрибут:

delivery_data — изначально пустой список адресов, по которым следует доставить письма
Экземпляр класса Postman должен иметь три метода экземпляра:

add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти
данные в виде кортежа:
(<улица>, <дом>, <квартира>)
get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице,
в которые требуется доставить письма
get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом
доме, в которые требуется доставить письма
Примечание 1. Дома и квартиры в списках, возвращаемых методами get_houses_for_street() и get_flats_for_house(), должны
располагаться в том порядке, в котором они были добавлены. Если дом или квартира, находящаяся в одном и том же доме,
встречается в списке адресов delivery_data несколько раз, то должны быть указаны те из них, которые были добавлены
раньше.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))
Sample Output 1:

[]
[]
[]
Sample Input 2:

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
Sample Output 2:

[151, 90]
[74, 75]
"""


class Postman:
    def __init__(self, delivery_data=None):
        if delivery_data is None:
            self.delivery_data = []

    def add_delivery(self, st, blg, apt):
        data = tuple((st, blg, apt))
        if data not in self.delivery_data:
            self.delivery_data.append(data)

    def get_houses_for_street(self, st):
        return list(dict.fromkeys([data[1] for data in self.delivery_data if data[0] == st]))

    def get_flats_for_house(self, st, blg):
        return [data[2] for data in self.delivery_data if data[0] == st and data[1] == blg]
