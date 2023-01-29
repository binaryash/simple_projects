import turtle
import random
c = turtle.getscreen()
c.setup(height = 400, width = 500)
color = ["red", "orange", "blue", "green", "yellow", "purple"]
userinput = c.textinput(title = 'make your bet',prompt = 'Who do you think will win ? "red", "orange", "blue", "green", "yellow", "purple"')
y_pos = [-70,-40,-10,20,50,80]
at = []
hf = False

for i in range(0,6):
    a = turtle.Turtle(shape = 'turtle')
    a.penup()
    a.color(color[i])
    a.penup()
    a.goto(-230,y_pos[i])
    at.append(a)

if userinput:
    hf = True

while hf:
    for b in at:
        if b.xcor() > 230:
            hf = False
            wincol = b.pencolor()
            if wincol == userinput:
                print(f"{wincol} won")
            else:
                print(f"{wincol} won")
                print(f"{userinput} lost")
        rad = random.randint(1,10)
        b.forward(rad)

c.exitonclick()
