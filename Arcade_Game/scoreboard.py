from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, font=("Arial",80,"normal"),align="center")
        self.goto(100,200)
        self.write(self.r_score, font=("Arial",80,"normal"),align="center")

    def l_point(self):
        self.l_score += 1
        self.scoreboard_update()

    def r_point(self):
        self.r_score += 1
        self.scoreboard_update()

        




