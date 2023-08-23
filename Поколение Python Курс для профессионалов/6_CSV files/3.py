"""
нкция csv_columns()
Реализуйте функцию csv_columns(), которая принимает один аргумент:

filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список
элементов этого столбца.

Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки не
используются.

Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.

Примечание 3. Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4
Anri,5
то следующий вызов функции csv_columns():

csv_columns('exam.csv')
должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.

Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую функцию csv_columns(), но не код,
вызывающий ее.

Примечание 6. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
"""
import csv


def csv_columns(filename: str) -> dict:
    with (open('C:/Users/kandz/Downloads/' + filename, encoding='utf-8') as f):
        data_list = list(csv.DictReader(f, delimiter=';'))
        data_dict = dict()
        for d in data_list:
            for k in d.keys():
                data_dict[k] = data_dict.get(k, []) + [d[k]]
        return data_dict

# ********************************************************************************************************************


def csv_columns_best(filename):

    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))
        return {key: value for key, *value in zip(*rows)}
    