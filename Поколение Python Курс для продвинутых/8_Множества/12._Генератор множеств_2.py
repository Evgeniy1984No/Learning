"""
Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов c
расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением, все на одной
строке, в нижнем регистре, в алфавитном порядке через пробел.

Примечание. Если бы список files содержал следующие имена файлов:

files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', '
github.git', 'ZeBrA.PnG']
"""
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
s_files = {word.lower() for word in files if word[-3:].lower() == 'png'}
result = {c.lower() for c in files if c.lower().endswith('.png')} # Оптимальное реешение
print(*sorted(s_files))