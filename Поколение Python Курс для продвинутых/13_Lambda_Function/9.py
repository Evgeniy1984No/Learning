"""
Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала
координат (точки (0;0). Программа должна вывести отсортированный список.

Примечание. Расстояние от начала координат до точки А равно ОА = (x**2 + y**2)**0.5
"""
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def distance_point(point):
    return (point[0]**2 + point[1]**2)**0.5


points.sort(key=distance_point)
print(points)