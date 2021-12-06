import turtle
import random

turtle.speed(10)
turtle.setheading(0)


def polygon(x, y, size, n, clr):
    turtle.penup()
    turtle.color(clr)
    turtle.fillcolor(clr)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(size)
        turtle.left(360 / n)
    turtle.end_fill()


color = "red green blue ".split()
for_color = random.choice(color)
for i in range(15):
    for_x = random.randint(-250, 250)
    for_y = random.randint(-250, 250)
    for_size = random.randint(10, 100)
    for_n = random.randint(3, 8)
    polygon(for_x, for_y, for_size, for_n, for_color)
