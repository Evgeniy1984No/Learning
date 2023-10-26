"""
Функция best_sender()
Рассмотрим два списка:

messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']

senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
Первый список представляет набор отправленных сообщений в некотором мессенджере, второй список — набор отправителей
этих сообщений. Причем сообщение messages[i] отправлено пользователем senders[i]. Каждое сообщение представляет собой
последовательность слов, разделенных пробелом (знаки препинания считаются частями слов). Количество слов — это общее
число слов, отправленное пользователем. Обратите внимание, что каждый пользователь может отправлять более одного
сообщения. Например, пользователь Sam Fisher отправил
2
2 слова в первом сообщении и
4
4 слова во втором, следовательно, его количество слов равно
2
+
4
=
6
2+4=6.

Реализуйте функцию best_sender(), которая принимает два аргумента в следующем порядке:

messages — список сообщений
senders — список имен отправителей
Функция должна определять отправителя, имеющего наибольшее количество слов, и возвращать его имя. Если таких
отправителей несколько, следует вернуть имя того, чье имя больше в лексикографическом сравнении.

Примечание 1. Гарантируется, что длины передаваемых в функцию списков совпадают.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию best_sender(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))
Sample Output 1:

Sam Fisher
Sample Input 2:

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))
Sample Output 2:

Charlie
"""
from collections import defaultdict


def best_sender(messages, senders):
    res = defaultdict(int)
    for i in range(len(messages)):
        res[senders[i]] += len(messages[i].split())
    return max(res.items(), key=lambda x: (x[1], x[0]))[0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))
messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(type(best_sender(messages, senders)))