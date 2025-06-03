"""
Класс BirthInfo 🌶️
Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один
аргумент:

birth_date — дата рождения, представленная в одном из следующих вариантов:
экземпляр класса date
строка с датой в ISO формате
список или кортеж из трех целых чисел: года, месяца и дня
Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено
исключение TypeError с текстом:

Аргумент переданного типа не поддерживается
Экземпляр класса BirthInfo должен иметь один атрибут:

birth_date — дата рождения в виде экземпляра класса date
Класс BirthInfo должен иметь одно свойство:

age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет,
прошедших с даты рождения на сегодняшний день
Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его
возраст увеличивается на один год.

Приведенный ниже код:

birthinfo = BirthInfo(date(2023, 2, 26))

print(birthinfo.age)
в 2024-02-25 должен выводить:

0
в 2024-02-26 должен выводить:

1
в 2025-02-25 должен выводить:

1
 в 2025-02-26 должен выводить:

2
Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию
current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.

Примечание 3. Никаких ограничений касательно реализации класса BirthInfo нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)
Sample Output 1:

2020-09-18
2010-10-10
2016-01-01
Sample Input 2:

birthday = date(2020, 9, 18)
today = date.today()
birthinfo = BirthInfo(birthday)
true_age = current_age(birthday, today)

print(birthinfo.age == true_age)
Sample Output 2:

True
"""
from functools import singledispatchmethod
from datetime import date, timedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        self.age = None
        self.birth_date = birth_date
        raise TypeError("Аргумент переданного типа не поддерживается")

    @staticmethod
    def get_age(d: date):
        current_day = date.today()
        if d.replace(year=current_day.year) > current_day:
            return current_day.year - d.year - 1
        return current_day.year - d.year

    @__init__.register(date)
    def date_init(self, birth_date):
        self.age = BirthInfo.get_age(birth_date)
        self.birth_date = birth_date

    @__init__.register(str)
    def str_init(self, s):
        try:
            d = date.fromisoformat(s)
            self.age = BirthInfo.get_age(d)
            self.birth_date = d
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register
    def list_tuple_init(self, data: list|tuple):
        try:
            y, m, d = data
            date_d = date(y, m, d)
            self.age = BirthInfo.get_age(date_d)
            self.birth_date = date_d
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")


birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)