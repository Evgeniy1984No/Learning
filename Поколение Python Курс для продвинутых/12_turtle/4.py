import turtle


def my_square_8(side):
    for n in range(2):
        for i in range(4):
            for _ in range(4):
                turtle.forward(side)
                turtle.left(90)
            turtle.right(90)
        turtle.right(45)


my_square_8(int(input()))
a = input()