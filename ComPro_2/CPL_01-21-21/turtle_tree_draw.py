import turtle

def tree_draw(level, size):
    if level == 0:
        return
    turtle.forward(size)
    turtle.left(90)
    tree_draw(level - 1, size*0.70)
    turtle.right(90)
    turtle.right(90)
    tree_draw(level - 1, size*0.70)
    turtle.left(90)
    turtle.forward(-1*size)

turtle.speed(0)
turtle.setheading(90)
turtle.pensize(4)
turtle.color('green')
tree_draw(10, 200)

turtle.done()
