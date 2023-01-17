"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:

Yes
Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html
Sample Output 2:

No
Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 3:

Yes


"""

import requests
import re
from bs4 import BeautifulSoup


def search_urls(url):
    res = requests.get(f"{url}")
    match = re.findall(r"<a href=\"(http\S+)\"", res.text)
    print('MATCH=', match)
    print('FUNC.TEXT=', res.text)
    return match
    # urls = []
    # page = requests.get(url)
    # soup = BeautifulSoup(page.text, "html.parser")
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    #     urls.append(link.get('href'))
    # return urls


a, b = (input() for _ in range(2))
urls_a = search_urls(a)
lst_urls_in = []
# for url_in_a in urls_a:
#     print('URL_IN_A=', url_in_a)
#     print('SEARCH_URLS(URL_IN_A)=', urls_a)
#     if b in search_urls(url_in_a):
#         print('Yes')
#     else:
#         if b in urls_a:
#             print('No')

for url_in_a in urls_a:
    lst_urls_in.extend(search_urls(url_in_a))
print(lst_urls_in)
if b in lst_urls_in:
    print('Yes')
else:
    if b in urls_a:
        print('No')
