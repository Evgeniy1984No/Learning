"""
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text
будет подсчитано количество его вхождений.
"""
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for i in text:
    result[i] = result.get(i, 0) + 1
