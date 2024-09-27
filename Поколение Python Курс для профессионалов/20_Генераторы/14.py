# Функция filter_names()
# Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
#
# names — список имен
# ignore_char — одиночный символ
# max_names — натуральное число
# Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
#
# начинаются на ignore_char (в любом регистре)
# содержат хотя бы одну цифру
# Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного
# списка.
#
# Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_names(), но не
# код, вызывающий ее.
#
# Примечание 3. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
#
# print(*filter_names(data, 'D', 3))
# Sample Output 1:
#
# Timur Arthur Arina
# Sample Input 2:
#
# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
#
# print(*filter_names(data, 't', 20))
# Sample Output 2:
#
# Dima Arthur Arina German Ruslan
# Sample Input 3:
#
# data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123',
# 'Geo000000r']
#
# print(*filter_names(data, 'A', 100))
# Sample Output 3:


def filter_names(names, ignore_char, max_names):
    res = (name for name in names if not name.lower().startswith(ignore_char.lower()) and name.isalpha())
    for _ in range(max_names):
        try:
            yield next(res)
        except StopIteration:
            break

# ********************************************************************************************************************


def best_filter_names(names, ignore_char, max_names):
    ignore_char = ignore_char.lower()
    filtred_char = (name for name in names if not name.lower().startswith(ignore_char))
    filtred_dig = (name for name in filtred_char if name.isalpha())
    return (name for idx, name in enumerate(filtred_dig) if idx < max_names)


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'A', 8))