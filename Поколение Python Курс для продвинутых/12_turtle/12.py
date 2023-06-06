import turtle


def zig(side=1):
    for i in range(10):
        for _ in range(4):
            turtle.left(90)
            turtle.forward(side)
            side += 2
    turtle.left(90)
    turtle.forward(side)


zig()
input()