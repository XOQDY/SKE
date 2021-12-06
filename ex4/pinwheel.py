import turtle
import random
turtle.speed(5)
clr_list = ['red', 'blue', 'gold', 'brown', 'violet', 'pink', 'orange', 'yellow']


def pinwheel(num_branch, size, backup):
    turtle.penup()
    turtle.pensize(random.randint(1, 35))
    turtle.color(clr_list[random.randint(0, 7)])
    turtle.goto(random.randint(-300, 300), random.randint(-200, 200))
    turtle.pendown()
    for x in range(num_branch):
        turtle.forward(size)
        turtle.backward(backup)
        turtle.left(360 / num_branch)


for i in range(10):
    num_branch_random = random.randint(6, 15)
    size_random = random.randint(50, 150)
    backup_random = random.randint(0, 100)
    pinwheel(num_branch_random, size_random, backup_random)
