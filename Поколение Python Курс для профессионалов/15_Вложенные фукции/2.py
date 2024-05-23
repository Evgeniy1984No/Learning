"""
Функция sourcetemplate()
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного
 знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
Реализуйте функцию sourcetemplate(), которая принимает один аргумент:

url — URL адрес
Функция sourcetemplate() должна возвращать функцию, которая принимает произвольное количество именованных аргументов
и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов. При вызове без
аргументов она должна возвращать исходный url адрес без изменений.

Примечание 1. Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию sourcetemplate(), но не
код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))
Sample Output 1:

https://beegeek.ru?name=timur
Sample Input 2:

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))
Sample Output 2:

https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165
Sample Input 3:

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())
Sample Output 3:

https://beegeek.ru
"""


def sourcetemplate(url):
    def query_string(**kwargs):
        if not kwargs:
            return url
        query = [f'{i}={kwargs[i]}' for i in sorted(kwargs)]
        return f'{url}?{"&".join(query)}'
    return query_string


url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())
