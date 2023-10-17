"""
Функция extract_this()
Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:

zip_name — название zip архива, например, data.zip
*args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного
названия файла для извлечения, то функция должна извлечь все файлы из архива.

Примечание 1. Например, следующий вызов функции

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.

Вызов функции

extract_this('workbook.zip')
должен извлечь из архива workbook.zip все файлы в папку с программой.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию extract_this(), но не код,
вызывающий ее.
"""
from zipfile import ZipFile


def extract_this(*args):
    with ZipFile(args[0]) as zip_file:
        if len(args) > 1:
            [zip_file.extract(i) for i in args[1:]]
        else:
            zip_file.extractall()


"""
У метода extractall() есть необязательный аргумент members, по умолчанию имеет значение None. Если ему не передавать 
никакие другие значения, то он принимает список всех файлов из архива.
Если же мы передадим в args названия файлов, которые нужно извлечь, то members примет кортеж файлов и извлечет их.
Если же в args ничего не передавать, тогда members примет пустой кортеж и ничего извлекать вообще не будет. Это 
отличается от поведения по умолчанию, которое было описано выше. Для этого и нужна проверка на пустой кортеж.
Если кортеж пуст, присваиваем переменной args значение None, и тогда извлекутся все файлы.
"""


def extract_this_best(zip_name: str, *args):
    if not args:
        args = None
    with ZipFile(zip_name) as zf:
        zf.extractall(members=args)


def extract_this_best_SHORT(zip_name: str, *args):
    with ZipFile(zip_name) as zf:
        zf.extractall(members=args or None)
