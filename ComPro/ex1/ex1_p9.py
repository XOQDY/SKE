import turtle
turtle.speed(1)
turtle.setheading(0)

# draw first pic
# draw blue six hexagon
turtle.penup()
turtle.color("blue")
turtle.goto(-120, 100)
turtle.pensize(5)
turtle.pendown()
turtle.circle(40, 360, 6)

# draw green six hexagon
turtle.left(90)
turtle.color("red")
turtle.circle(40, 360, 6)

# draw yellow six hexagon
turtle.left(90)
turtle.color("yellow")
turtle.circle(40, 360, 6)

# draw red six hexagon
turtle.left(90)
turtle.color("green")
turtle.circle(40, 360, 6)


# draw second pic
# draw blue square
turtle.penup()
turtle.pensize(0)
turtle.goto(-200, -120)
turtle.setheading(0)
turtle.color("blue")
turtle.fillcolor("blue")
turtle.pendown()
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.end_fill()

# draw diagonal bottom left - top right
turtle.color("white")
turtle.fillcolor("white")
turtle.begin_fill()
turtle.forward(30)
turtle.goto(0, -30)
turtle.goto(0, 0)
turtle.goto(10, 0)
turtle.goto(-200, -110)
turtle.end_fill()

# draw diagonal top right - bottom left
turtle.penup()
turtle.goto(-30, -120)
turtle.pendown()
turtle.begin_fill()
turtle.forward(30)
turtle.goto(0, -110)
turtle.goto(-210, 0)
turtle.goto(-230, 0)
turtle.goto(-230, -15)
turtle.goto(-30, -120)
turtle.end_fill()

# draw white square bottom-top
turtle.penup()
turtle.goto(-120, -120)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-80, -120)
turtle.goto(-80, -20)
turtle.goto(-120, -20)
turtle.goto(-120, -120)
turtle.end_fill()

# draw white square left-right
turtle.penup()
turtle.goto(-200, -90)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-200, -50)
turtle.goto(0, -50)
turtle.goto(0, -90)
turtle.goto(-200, -90)
turtle.end_fill()

# draw red square bottom-top
turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(-115, -120)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-85, -120)
turtle.goto(-85, -20)
turtle.goto(-115, -20)
turtle.end_fill()

# draw red square left-right
turtle.penup()
turtle.goto(-200, -85)
turtle.begin_fill()
turtle.goto(0, -85)
turtle.goto(0, -55)
turtle.goto(-200, -55)
turtle.end_fill()

# draw red diagonal bottom left - top right
turtle.penup()
turtle.goto(-200, -120)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-175, -120)
turtle.goto(0, -20)
turtle.goto(-25, -20)
turtle.goto(-200, -120)
turtle.end_fill()

# draw red diagonal top right - bottom left
turtle.penup()
turtle.goto(-200, -20)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-175, -20)
turtle.goto(0, -120)
turtle.goto(-25, -120)
turtle.goto(-200, -20)
turtle.end_fill()


# draw sign traffic light
# draw yellow square
turtle.penup()
turtle.goto(150, 30)
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.circle(100, 360, 4)
turtle.end_fill()

# draw black square
turtle.penup()
turtle.goto(150, 35)
turtle.color("black")
turtle.pensize(3)
turtle.pendown()
turtle.circle(95, 360, 4)

# draw black traffic light
turtle.penup()
turtle.goto(130, 80)
turtle.pensize(0)
turtle.pendown()
turtle.begin_fill()
turtle.goto(170, 80)
turtle.goto(170, 180)
turtle.goto(130, 180)
turtle.goto(130, 80)
turtle.end_fill()

# draw green circle
turtle.penup()
turtle.color("green")
turtle.fillcolor("green")
turtle.goto(150, 85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(13.5)
turtle.end_fill()

# draw yellow circle
turtle.penup()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.goto(150, 117)
turtle.pendown()
turtle.begin_fill()
turtle.circle(13.5)
turtle.end_fill()

# draw red circle
turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(150, 149)
turtle.pendown()
turtle.begin_fill()
turtle.circle(13.5)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
