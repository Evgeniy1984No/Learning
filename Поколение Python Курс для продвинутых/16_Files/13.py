"""
Загадка от Жака Фреско 🌶️
Однажды Жака Фреско спросили:

"Если ты такой умный, почему не богатый?"

Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:

"Были разноцветные козлы. Сколько?"

"Сколько чего?"

"Сколько из них составляет более 7% от общего количества козлов?"

Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных
цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень
козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от
Жака Фреско.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, которые
удовлетворяют условию загадки Жака Фреско.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл goats.txt содержал строки:

COLOURS
Pink goat
Green goat
Black goat
GOATS
Pink goat
Pink goat
Black goat
Pink goat
Pink goat
Black goat
Green goat
Pink goat
Black goat
Black goat
Pink goat
Pink goat
Black goat
Black goat
Pink goat
то файл answer.txt имел бы вид:

Black goat
Pink goat
"""
with open('C:/Users/kandz/Downloads/goats.txt', encoding='utf-8') as file_in, \
        open('C:/Users/kandz/Downloads/answer.txt', 'w', encoding='utf-8') as file_out:
    colours = set()
    s = 0
    lst = file_in.read().split('\n')
    answer = list()
    for line in lst:
        if line not in ('COLOURS', 'GOATS'):
            colours.add(line)
            s += 1
    s = s - len(colours)
    for elem in colours:
        count = lst.count(elem) - 1
        if count * 100 > 7 * s:
            answer.append(elem)
    [print(i, file=file_out) for i in sorted(answer)]

# **********************************************************************************************************************
with open('C:/Users/kandz/Downloads/goats.txt') as f1, open('C:/Users/kandz/Downloads/answer.txt', 'w') as f2:
    cont = f1.read().split('\n')
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)