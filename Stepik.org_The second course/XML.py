"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики,
расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3.
И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1
"""

# from xml.etree.ElementTree import XMLParser
#
#
# class MaxDepth:
#     maxDepth = 0
#     depth = 0
#     attrib_weight = {}
#
#     def start(self, tag, attrib):
#         # print('tag=', tag, 'attrib=', attrib)
#         self.depth += 1
#         # print('depth=', self.depth)
#         if attrib['color'] not in self.attrib_weight:
#             self.attrib_weight[attrib['color']] = self.depth
#         else:
#             self.attrib_weight[attrib['color']] += self.depth
#         if self.depth > self.maxDepth:
#             self.maxDepth = self.depth
#
#     def end(self, tag):
#         self.depth -= 1
#
#     def data(self, data):
#         pass
#
#     def close(self):
#         return self.attrib_weight
#         # return self.maxDepth
#
#
# xml_string = input()
#
# target = MaxDepth()
# parser = XMLParser(target=target)
#
# parser.feed(xml_string)
# weights_of_colors = parser.close()
# print(weights_of_colors['red'], weights_of_colors['green'], weights_of_colors['blue'])

"""
____________________________________________________________________________________________________________
"""

from xml.etree import ElementTree

xml_example = input()
root = ElementTree.fromstring(xml_example)
colors = {"red": 0, "green": 0, "blue": 0}
print(root.attrib)


def getcubes(root, value):
    colors[root.attrib['color']] += value
    for child in root:
        getcubes(child, value + 1)


getcubes(root, 1)
print(colors["red"], colors["green"], colors["blue"])
