import turtle


def draw_square(size):
    '''Draw a square around its center whose size is determined by the input argument size
    '''
    turtle.penup()
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(-size / 2)
    turtle.right(90)
    turtle.forward(-size / 2)


def recurse_draw_square(level, size, x, y):
    if level == 0:
        return

    turtle.penup()
    turtle.goto(x, y)
    draw_square(size)
    # you fill in the rest of the code
    recurse_draw_square(level - 1, size / 2, x - size / 2, y + size / 2)
    recurse_draw_square(level - 1, size / 2, x + size / 2, y + size / 2)
    recurse_draw_square(level - 1, size / 2, x - size / 2, y - size / 2)
    recurse_draw_square(level - 1, size / 2, x + size / 2, y - size / 2)


# you may want to set speed to zero if you want to run at the fastest speed
turtle.speed(0)
turtle.setheading(0)
turtle.goto(0, 0)
# to draw a square whose size is 200 and centered at (0, 0)
# draw_square(200)
# turtle.goto(0 - 200 / 2, 0 + 200 / 2)
# # to draw a square whose size is 200/2 and centered at (0 - 200/2, 0 + 200/2)
# draw_square(200 / 2)

turtle.clear()
recurse_draw_square(4, 200, 0, 0)

turtle.done()
