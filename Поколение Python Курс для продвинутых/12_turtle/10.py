import turtle


side = int(input())
angle = 0
turtle.speed(1)
for _ in range(12):
    turtle.forward(side)
    turtle.backward(side)
    angle += 30
    turtle.setheading(angle)
input()