import turtle


def diamond(side):
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)


def snowflake(side):
    angle = 0
    for _ in range(10):
        diamond(side)
        angle += 36
        turtle.setheading(angle)


snowflake(int(input()))

input()