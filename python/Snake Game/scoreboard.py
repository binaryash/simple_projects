from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,230)
        self.write (f"Scoreboard :{self.score}",move = False, align = 'center', font = ('Arial','24','normal'))
        self.hideturtle()

    def increase_sc(self):
        self.score+=1
        self.clear()
        self.write (f"Scoreboard : {self.score}",move = False, align = 'center', font = ('Arial','24','normal'))

    def game_over(self):
        self.goto(0,0)
        self.write ("GAME OVER",move = False, align = 'center', font = ('Arial','30','normal'))