import turtle


def my_square(side):
    for _ in range(3):
        turtle.left(22.5)
        for s in range(4):
            turtle.forward(side)
            turtle.left(90)


turtle.setheading(15)
turtle.speed(30)


def square(side):
    for i in range(1, 181):
        turtle.setheading(2 * i)
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)


a = int(input())

print(square(a))

b = input()