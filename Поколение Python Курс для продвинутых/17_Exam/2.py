"""
Goooood students
Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров. Строки файла
имеют вид: фамилия оценка_1 оценка_2 оценка_3.

Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным, если количество
баллов по нему не меньше
65
65.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести количество студентов, сдавших все три теста.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Если бы файл grades.txt содержал строки:

Washington 83 77 54
Adams 86 69 90
Jacobson 50 49 71
MacDonald 100 99 100
Berrington 66 67 64
то результатом будет:

2
"""


def success(student):
    for ind in range(1, len(student)):
        if int(student[ind]) < 65:
            return False
    return True


with open('C:/Users/kandz/Downloads/grades.txt', encoding='utf-8') as file:
    lst = [line.strip().split() for line in file.readlines()]
    print(len(list(filter(lambda x: success(x), lst))))
# **********************************************************************************************************************
with open('C:/Users/kandz/Downloads/grades.txt', encoding='utf-8') as f:
    print(sum(1 for i in f.readlines() if all([int(j) >= 65 for j in i.split(' ')[1:]])))
    