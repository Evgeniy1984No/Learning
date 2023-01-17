"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением
случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

url = input()
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, "html.parser")  # , parse_only=only_a_tags)
lst = []
for link in soup.find_all('a'):
    # print(link.get('href'))
    link = urlparse(link.get('href')).hostname
    if link not in lst and link is not None:
        lst.append(link)

lst = sorted(lst)

for _ in lst:
    print(_)

"""
______________________________________________________________________________________________________
"""

import urllib.parse as urllib
from lxml import html

url = input().rstrip()
page = requests.get(url)
tree = html.fromstring(page.text)
hrefs = tree.xpath('//a/@href')
url_set = set()
for link in hrefs:
    line = urllib.urlsplit(link)[1] if urllib.urlsplit(link)[1] else urllib.urlsplit(link)[2]
    if line[0].isalpha():
        url_set.add(line.split(':')[0]) if len(line.split(':')) > 1 else url_set.add(line)
[print(x) for x in sorted(url_set)]
