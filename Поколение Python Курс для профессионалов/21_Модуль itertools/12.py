# Нет дел
# Каждый день Тимур записывает в блокнот дела, которые ему нужно выполнить. Каждое дело он разбивает на несколько
# действий.
#
# Вам доступен список tasks, в котором записаны все дела Тимура. Каждый элемент списка представляет собой кортеж из
# трех элементов: первый — название дела, второй — действие, третий — очередность.
#
# Дополните приведенный ниже код, чтобы он вывел все дела Тимура в алфавитном порядке, указав для каждого набор
# соответствующих действий в правильной очередности, в следующем формате:
#
# <дело>:
#     1. <действие>
#     2. <действие>
#     ...
# Между двумя делами должна быть расположена пустая строка.
#
# Примечание 1. Начальная часть ответа выглядит так (в качестве отступов используйте четыре пробела):
#
# ЕГЭ Математика:
#     1. доделать курс по параметрам
#
# Курс по ооп:
#     1. обсудить темы
#     2. обсудить задачи
#
# ...
from itertools import groupby

tasks = [('Отдых', 'поспать днем', 3),
         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
         ('Отдых', 'погулять вечером', 4),
         ('Курс по ооп', 'обсудить темы', 1),
         ('Урок по groupby', 'добавить задачи на программирование', 3),
         ('Урок по groupby', 'написать конспект', 1),
         ('Отдых', 'погулять днем', 2),
         ('Урок по groupby', 'добавить тестовые задачи', 2),
         ('Уборка', 'убраться в ванной', 2),
         ('Уборка', 'убраться в комнате', 1),
         ('Уборка', 'убраться на кухне', 3),
         ('Отдых', 'погулять утром', 1),
         ('Курс по ооп', 'обсудить задачи', 2)]
tasks_sort = sorted(tasks, key=lambda x: (x[0], x[2]))
tasks_group = groupby(tasks_sort, key=lambda y: y[0])
for k, v in tasks_group:
    print(f'{k}:')
    [print(f'    {i[2]}. {i[1]}') for i in v]
    print()
