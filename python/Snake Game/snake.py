import turtle
st_pos = [(0,0),(-20,0),(-40,0)]
move_dist = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for i in st_pos:
             self.add_segment(i)


    def add_segment(self,i):
        t = turtle.Turtle('square')
        t.color('white')
        t.penup()
        t.goto(i)
        self.seg.append(t)

    def move(self):
        for j in range(len(self.seg)-1,0,-1):
            xcoor = self.seg[j - 1].xcor()
            ycoor= self.seg[j - 1].ycor()
            self.seg[j].goto(xcoor,ycoor)
        self.seg[0].forward(move_dist)

    def extend(self):
         self.add_segment(self.seg[-1].position())

    def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

    def down(self):
            if self.head.heading() != UP:    
                self.head.setheading(DOWN)

    def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

    def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)


