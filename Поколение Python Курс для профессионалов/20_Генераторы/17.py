# Функция nonempty_lines()
# Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:
#
# file — название текстового файла, например, data.txt
# Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным
# символом переноса строки \n. Если строка содержит более
# 25
# 25 символов, она заменяется многоточием ....
#
# Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию nonempty_lines(), но не
# код, вызывающий ее.
#
# Примечание 3. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# lines = nonempty_lines('file1.txt')
#
# print(next(lines))
# print(next(lines))
# print(next(lines))
# print(next(lines))
# Sample Output 1:
#
# bee
# geek
# stepik
# aaaaaaaaaaaaaaaaaaaaaaaaa
# Sample Input 2:
#
# print(*nonempty_lines('file2.txt'))
# Sample Output 2:
#
# short line another short line ... end of file

def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        yield from ('...' if len(line.rstrip()) > 25 else line.rstrip() for line in f if line.rstrip())
