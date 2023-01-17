"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No",
если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No

10
classA : classB classC classD classG classH
classB : classC classE classG classH classK classL
classC : classE classD classH classK classL
classE : classD classF classK classL classC
classD : classG classH
classF : classK
classG : classF
classH : classL
classK : classH classL
classL
"""

classes = {}

for n in range(int(input())):
    f = input().split()
    # print(f)
    if len(f) == 1:
        classes.update({f[0]: []})
        # print(classes)
    else:
        lst = []
        for i in range(2, len(f)):
            lst.append(f[i])
        classes.update({f[0]: lst})


print(classes)


def is_parent(p_parent, child):
    if p_parent in classes[child] or p_parent == child:
        return True
    if classes.get(child) == [] or child not in classes:
        return False
    else:
        for parent in classes[child]:
            if is_parent(p_parent, parent):
                return True
        # res = []
        # for parent in classes[child]:
        #     res.append(is_parent(p_parent, parent))
        # return True in res


# answ = []
for n in range(int(input())):
    pre_parent, child = input().split()
    if is_parent(pre_parent, child):
        print('Yes')
        # answ.append('Yes')
    else:
        print('No')
        # answ.append('No')
# print(*answ, sep='\n')
'''
_______________________________________________________________________________________________________________
'''


def test(parent, child):
    if parent == child or parent in base[child]:
        return 'Yes'
    for _ in base[child]:
        if test(parent, _) == 'Yes':
            return 'Yes'
    return 'No'


base = {}
for com in [input().split(' ') for i in range(int(input()))]:
    base[com[0]] = com[2:len(com)]
for com in [input().split(' ') for i in range(int(input()))]:
    print(test(com[0], com[1]))
