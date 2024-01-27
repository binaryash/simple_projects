import turtle
hf = 3
t = turtle.Turtle()
colo = ["teal","wheat","lime","slate blue","tomato"]
while hf <8:
    for i in range (hf):
        angle = 360/hf
        turtle.color(colo[hf-3])
        turtle.forward(90)
        turtle.right(angle)
    hf+=1

c = turtle.getscreen()
c.exitonclick()
