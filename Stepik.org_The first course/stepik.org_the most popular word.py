import os

input_file = 'dataset_3363_3.txt'
path = os.path.join('D:/', 'Google Drive', 'PycharmProjects', 'Learning', input_file)
count = 0
d = {}

with open(path) as txt:
    line = txt.read().lower().strip().split()
line.sort()

for word in line:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if count < d[word]:
        word_pop = word
        count = d[word]

print(word_pop, count)

