import turtle


side = int(input())
for _ in range(2):
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.setheading(180)
input()