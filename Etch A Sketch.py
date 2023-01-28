import turtle
t = turtle.Turtle()
c = turtle.getscreen()
t.speed('fastest')
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_right():
    return t.setheading (t.heading ()+ 10)

def move_left():
    return t.setheading(t.heading() - 10)

c.listen()
c.onkey(move_forward,"w")
c.onkey(move_backward,"s")
c.onkey(move_right,"d")
c.onkey(move_left,"a")

c.exitonclick()
