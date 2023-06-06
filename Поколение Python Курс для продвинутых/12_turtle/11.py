import turtle


def square(side):
    for _ in range(4):
        turtle.left(90)
        turtle.forward(side)


def more_square(n):
    side = 10
    for _ in range(n):
        square(side)
        side += n / 20


more_square(int(input()))
input()