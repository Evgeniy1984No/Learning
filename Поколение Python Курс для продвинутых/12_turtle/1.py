"""
Напишите программу, которая рисует прямоугольник.



Примечание. Программу нужно оформить в виде функции rectangle(width, height), где width,
height – ширина и высота прямоугольника.
"""
import turtle


def rectangle(width, height):
    turtle.forward(width)
    turtle.setheading(90)

    turtle.forward(height)
    turtle.setheading(180)

    turtle.forward(width)
    turtle.setheading(270)

    turtle.forward(height)


# **************************************************************************
def rectangle_best(width_best, height_best):
  for _ in range(4):
    turtle.forward(width_best)
    turtle.left(90)
    width_best, height_best = height_best, width_best


rectangle_best(int(input()), int(input()))