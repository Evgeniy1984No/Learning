"""
Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и
оценка разделены пробелом). Оценка - целое число от
0
0 до
100
100 включительно.

Напишите программу для добавления
5
5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл class_scores.txt содержал строки:

Washington 83
Adams 86
Kingsman 100
MacDonald 95
Thomson 98
то файл new_scores.txt имел бы вид:

Washington 88
Adams 91
Kingsman 100
MacDonald 100
Thomson 100
"""
# with open('C:/Users/kandz/Downloads/class_scores.txt', encoding='utf-8') as file_in, \
#         open('C:/Users/kandz/Downloads/new_scores.txt', 'w', encoding='utf-8') as file_out:
#     lst = [line.split() for line in file_in.readlines()]
#     new_score = list()
#     for elem in lst:
#         if int(elem[1]) + 5 <= 100:
#             new_score.append([elem[0], int(elem[1]) + 5])
#         else:
#             new_score.append([elem[0], 100])
#     [print(f'{elem[0]} {int(elem[1])}', file=file_out) for elem in new_score]

with open('C:/Users/kandz/Downloads/class_scores.txt', encoding='utf-8') as file_in, \
        open('C:/Users/kandz/Downloads/new_scores.txt', 'w', encoding='utf-8') as file_out:
    lst = [line.split() for line in file_in.readlines()]
    [print(f'{elem[0]} {int(elem[1]) + 5 if int(elem[1]) <= 95 else 100}', file=file_out) for elem in lst]

with open('C:/Users/kandz/Downloads/new_scores.txt', encoding='utf-8') as file_out:  # Просто вывод файла
    print(file_out.readlines())

# ********************************************************************************************************************
with open('C:/Users/kandz/Downloads/class_scores.txt') as class_scores, \
        open('C:/Users/kandz/Downloads/new_scores.txt', 'w', encoding='utf-8') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=new_scores)
