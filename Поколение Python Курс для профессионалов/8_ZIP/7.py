"""
Структура архива 🌶️🌶️
Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую
структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так как архив
имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
"""
from zipfile import ZipFile


def hr_size(n, k=0):
    return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)


def converter_size(size):
    units = [('GB', 2 ** 30), ('MB', 2 ** 20), ('KB', 2 ** 10), ('B', 1)]
    for tup in units:
        size_file = (tup[0], size / tup[1])
        if size_file[1] >= 1:
            break
    return f'{round(size_file[1])} {size_file[0]}'


with ZipFile('C:/Users/kandz/Downloads/desktop.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        path = item.filename.strip('/').split('/')
        print('  ' * path.index(path[-1]) + path[-1] + ('' if item.is_dir() else ' ' + converter_size(item.file_size)))
