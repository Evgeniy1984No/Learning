"""
Файлы в файле 🌶️🌶️
Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и
выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в
лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с
округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах,
а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB
Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 5. указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.


dict_files = {mp3: {names: [], B: int, KB: int, MB: int}}
"""
with (open('C:/Users/kandz/Downloads/files.txt', encoding='utf-8') as files):
    dict_files = dict()
    units = [('GB', 2 ** 30), ('MB', 2 ** 20), ('KB', 2 ** 10), ('B', 1)]
    for line in files.readlines():
        file = line.split()
        name, exten = file[0].split('.')
        size_name = sum(i[1] * int(file[1]) for i in units if i[0] == file[2])
        dict_files.setdefault(exten, {'names': [], 'Summary': 0})
        dict_files[exten]['names'].append(name + '.' + exten)
        dict_files[exten]['Summary'] += size_name
    sorted_dict_files = dict(sorted(dict_files.items()))
    for key in sorted_dict_files.keys():
        for tup in units:
            size_files = (tup[0], round(sorted_dict_files[key]['Summary'] / tup[1]))
            if size_files[1] >= 1:
                break
        print(*sorted(sorted_dict_files[key]['names']), sep='\n')
        print('----------')
        print(f'Summary: {size_files[1]} {size_files[0]}')
        print()





