"""
Класс Person
Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем
порядке:

name — имя человека
surname — фамилия человека
Экземпляр класса Person должен иметь два атрибута:

name — имя человека
surname — фамилия человека
Класс Person должен иметь одно свойство:

fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении
полного имени должны изменяться имя и фамилия.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)
Sample Output 1:

Меган
Фокс
Меган Фокс
Sample Input 2:

person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)
Sample Output 2:

Стефани Фокс
Sample Input 3:

person = Person('Алан', 'Тьюринг')

person.surname = 'Вирт'
print(person.fullname)
Sample Output 3:

Алан Вирт
Sample Input 4:

person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)
Sample Output 4:

Алан
Тьюринг
"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + ' ' + self.surname

    def set_fullname(self, new_name_new_surname):
        new_name, new_surname = new_name_new_surname.split()
        self.name = new_name
        self.surname = new_surname

    fullname = property(get_fullname, set_fullname)