# Я в аду?
# Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:
#
# 7-ddd-ddd-dd-dd
# 8-ddd-dddd-dddd
# где d — цифра от
# 0
# 0 до
# 9
# 9.
#
# Формат входных данных
# На вход программе подается строка произвольного содержания.
#
# Формат выходных данных
# Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи,
# и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.
#
# Примечание. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# Перезвони мне, пожалуйста: 7-919-667-21-19
# Sample Output 1:
#
# 7-919-667-21-19
# Sample Input 2:
#
# Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911
# Sample Output 2:
#
# 7-919-667-21-19
# 8-917-4864-1911
s = input()


def is_phone_number(phone):
    groups = phone.split('-')
    # 7-ddd-ddd-dd-dd
    # 8-ddd-dddd-dddd
    if phone[0] not in '78' and len(groups) < 5:
        return False
    if len(groups) == 5:
        if tuple(map(len, groups)) != (1, 3, 3, 2, 2):
            return False
    if len(groups) == 4:
        if tuple(map(len, groups)) != (1, 3, 4, 4):
            return False
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars) and [len(chars) == 11, len(chars) == 12][phone[0] == '8']


def get_all_numbers(text):
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            yield chunk


[print(i) for i in get_all_numbers(s)]