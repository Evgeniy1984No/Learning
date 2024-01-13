"""
Уж лучше матрицы 😐
Назовем пароль хорошим, если

его длина равна
9
9 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра
Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.

Формат входных данных
На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них
присутствует хороший.

Формат выходных данных
Для каждого введенного пароля программа должна вывести текст:

LengthError, если длина введенного пароля меньше
9
9 символов
LetterError, если в нем все буквы имеют одинаковый регистр либо отсутствуют
DigitError, если в нем нет ни одной цифры
Success!, если введенный пароль хороший
После ввода хорошего пароля все последующие пароли должны игнорироваться.

Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий: LengthError, затем
LetterError, а уже после DigitError.

Примечание 2. Воспользуйтесь функцией is_good_password() из предыдущей задачи.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

arr1
Arrrrrrrrrrr
arrrrrrrrrrrrrrr1
Arrrrrrr1
Sample Output 1:

LengthError
DigitError
LetterError
Success!
Sample Input 2:

beegeek
Beegeek123
Beegeek2022
Beegeek2023
Beegeek2024
Sample Output 2:

LengthError
Success!
"""
import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str):
    pwd = string
    if len(string) < 9:
        raise LengthError('LengthError')
    elif not all((any(map(str.isupper, pwd)), any(map(str.islower, pwd)))):
        raise LetterError('LetterError')
    elif not any(map(str.isdecimal, pwd)):
        raise DigitError('DigitError')
    return 'Success!'


for line in sys.stdin:
    try:
        print(is_good_password(line.strip()))
        break
    except PasswordError as e:
        print(e)
