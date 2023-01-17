import requests

input_file = '699991.txt'

while True:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + input_file)
    txt = r.text.splitlines()
    input_file = txt[0]
    if r.text.startswith('We'):
        print(r.text)
        break
    print(r.text)








