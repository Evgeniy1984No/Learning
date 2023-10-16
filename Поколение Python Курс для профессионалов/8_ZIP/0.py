"""
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное
число — количество файлов в этом архиве.

Примечание 1. Обратите внимание, что папка не считается файлом.

Примечание 2. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
"""
import zipfile
from zipfile import ZipFile

with ZipFile('C:/Users/kandz/Downloads/workbook.zip') as zip_file:
    info = zip_file.infolist()
    dirs_count = list(map(zipfile.ZipInfo.is_dir, info))
    print(len(dirs_count) - sum(dirs_count))
# ********************************************************************************************************************
    print(sum(not f.is_dir() for f in zip_file.infolist()))
    