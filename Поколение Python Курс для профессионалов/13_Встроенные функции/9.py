"""
Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно
следующим правилам:

все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед отсортированными четными
Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.

Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

Sorting1234
Sample Output 1:

ginortS1324
Sample Input 2:

n0tEast3rEgg
Sample Output 2:

aggnrsttEE30
Sample Input 3:

3DYrz34UXl
Sample Output 3:

lrzDUXY334
"""
s = input()


def unusual_sort(string: str) -> str:
    chars_up = sorted([i for i in string if i.isupper()])
    chars_low = sorted([i for i in string if i.islower()])
    dig_1 = sorted([i for i in string if i.isdigit() and int(i) % 2 != 0])
    dig_2 = sorted([i for i in string if i.isdigit() and int(i) % 2 == 0])
    return ''.join(chars_low + chars_up + dig_1 + dig_2)


print(unusual_sort(s))

# ********************************************************************************************************************


def comparator(char):
    if char.isalpha():
        return 0, char.isupper(), char
    digit = int(char)
    return 1, digit % 2 == 0, digit


print(''.join(sorted(s, key=comparator)))