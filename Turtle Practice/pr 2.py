import turtle
import random
t = turtle.Turtle()
colo = ["teal","wheat","lime","slate blue","tomato"]
dire = [90,180,270,360]
for i in range (100):
    a = random.choice(dire)
    t.speed("fastest")
    t.pensize(10)
    t.color(random.choice(colo))
    t.forward(20)
    t.setheading(a)
    


c = turtle.getscreen()
c.exitonclick()
