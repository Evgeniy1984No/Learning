"""
 Класс User
Реализуйте класс User, описывающий интернет-пользователя. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя. Если name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Экземпляр класса User должен иметь два атрибута:

_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:

get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name. Если
new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age. Если
new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с
текстом:
Некорректный возраст
Примечание 1. Если при создании экземпляра класса User имя и возраст одновременно являются некорректными, должно быть
возбуждено исключение, связанное с именем.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())
Sample Output 1:

Гвидо
67
Sample Input 2:

user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())
Sample Output 2:

Тимур
30
"""


class User:
    def __init__(self, name: str, age: int):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name: str):
        if not (isinstance(new_name, str) and new_name and new_name.isalpha()):
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not (isinstance(new_age, int) and 0 <= new_age <= 110):
            raise ValueError('Некорректный возраст')
        self._age = new_age
