import turtle


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)


def cells(side):
    for n in range(6):
        hexagon(side)
        turtle.right(120)
        turtle.forward(side)
        turtle.left(60)


cells(int(input()))
# hexagon(50)
input()
