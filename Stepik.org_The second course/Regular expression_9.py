"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz
Sample Output:

atraction
buz
"""

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # match = re.findall(r"((\w)\2+)", line)
    # print(match)
    # print(match.groups())
    print(re.sub(r"((\w)\2+)", r"\2", line))
