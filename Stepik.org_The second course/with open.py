"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""

with open("dataset_24465_4.txt", "r") as txt_orig, open("text_copy.txt", "w") as txt_copy:
    line = txt_orig.read().split('\n')
    line_rev = []
    for ind in range(len(line)-1, -1, -1):
        line_rev.append(line[ind])
        cont = "\n".join(line_rev)
    txt_copy.write(cont)


