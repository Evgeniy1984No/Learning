"""
Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену. Дополните
приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате
username@domain.

Примечание 1. Для сортировки в алфавитном порядке используйте встроенную функцию sorted(), либо списочный метод sort().

Примечание 2. Группировать электронные адреса по доменам не нужно.
"""
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']
          }
d = set()
for k, v in emails.items():
    for name in v:
        d.add(name + '@' + k)
print(*sorted(d), sep='\n')
"""
__________________________________________________________________________________
"""
print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')