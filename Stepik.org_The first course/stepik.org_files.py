with open('dataset_3363_2.txt') as arr_in:
    s = arr_in.readline().strip()

s_list = []
num = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

for i in range(len(s)):
    char = s[i]
    if char in num and i != len(s)-1:
        if s[i-1] in num:
            continue
        elif s[i+1] not in num:
            s_list.append(int(char))
        else:
            char_num = char + s[i+1]
            s_list.append(int(char_num))
    elif i != len(s)-1:
        s_list.append(char)

print(s_list)

with open('Outpu.txt', 'w') as arr_out:
    for j in range(len(s_list)):
        char = s_list[j]
        if type(char) == str:
            arr_out.write(char*s_list[j+1])
