"""
Проще, чем кажется 🌶️
Рассмотрим следующий текстовый фрагмент:

ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none
Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта, значение
свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого равно purple. Также у
объекта ball есть свойства size и notes, имеющие значения 4 и it's round соответственно. Помимо объекта ball имеется
объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее название object и сгруппируем строки
данного текстового фрагмента по первому столбцу:

object,color,size,notes
ball,purple,4,it's round
cup,blue,1,none
Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а в последующих —
значения соответствующих свойств этого объекта.

Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:

filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового фрагмента,
рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя объекта, свойство
этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
id_name — общее название для объектов
Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав первый
столбец id_name. Полученный результат функция должна записать в файл condensed.csv.

Примечание 1. Например, если бы файл data.csv имел следующий вид:

01,Title,Ran So Hard the Sun Went Down
02,Title,Honky Tonk Heroes (Like Me)
то вызов функции condense_csv():

condense_csv('data.csv', id_name='ID')
должен был бы создать файл condensed.csv со следующим содержанием:

ID,Title
01,Ran So Hard the Sun Went Down
02,Honky Tonk Heroes (Like Me)
Примечание 2. Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая, при этом кавычки не
используются.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию condense_csv(), но не код,
вызывающий ее.
"""
import csv

# text = '''01,Artist,Otis Taylor
# 01,Title,Ran So Hard the Sun Went Down
# 01,Time,3:52
# 02,Artist,Waylon Jennings
# 02,Title,Honky Tonk Heroes (Like Me)
# 02,Time,3:29
# 03,Artist,David Allan Coe
# 03,Title,Willie Waylon And Me
# 03,Time,3:26'''
#
# with open('data.csv', 'w', encoding='utf-8') as file:
#     file.write(text)


def condense_csv(filename: str, id_name: str):
    with open(filename, encoding='utf-8') as file_in:
        data = csv.reader(file_in, delimiter=',')
        dict_in = {}
        headers_list = [id_name]
        list_dicts = []
        for row in data:
            dict_in[row[0]] = dict_in.get(row[0], {})
            dict_in[row[0]][row[1]] = dict_in[row[0]].get(row[1], '') + row[2]
        for k, v in dict_in.items():
            temp = [k]
            for v_in in dict_in[k].values():
                temp.append(v_in)
            list_dicts.append(temp)
        [headers_list.append(l) for l in dict_in[k].keys()]

    with open('condensed.csv', 'w', encoding='utf-8') as file_out:
        writer = csv.writer(file_out, delimiter=',')
        writer.writerow(headers_list)
        writer.writerows(list_dicts)


# **************************************************************************************************************
def condense_csv_best(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        objects = {}
        for obj, attr, value in csv.reader(file):
            if obj not in objects:
                objects[obj] = {id_name: obj}
            objects[obj][attr] = value

    with open('condensed.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=objects[obj])
        writer.writeheader()
        writer.writerows(objects.values())


condense_csv('data.csv', id_name='ID')
