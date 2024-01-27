from snake import Snake
from scoreboard import ScoreBoard
import turtle
import time
from food import Food
c = turtle.getscreen()
c.setup(height = 600, width = 600)
c.bgcolor('black')
c.title('Classic Snake Game')
c.tracer(0)

s = Snake()
f = Food()
sc = ScoreBoard()

c.listen()
c.onkey(s.up ,"Up")
c.onkey(s.down ,"Down")
c.onkey(s.left ,"Left")
c.onkey(s.right ,"Right")

hf = True
while hf:
    c.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        sc.increase_sc()

    if s.head.xcor() > 290 or s.head.xcor() <-290 or s.head.ycor() > 290 or s.head.ycor() < -290:
        hf = False
        sc.game_over()

    for segment in s.seg[1:]:
        if s.head.distance(segment) < 10:
            hf = False
            sc.game_over()

c.exitonclick()
