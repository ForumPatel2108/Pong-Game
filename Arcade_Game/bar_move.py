from turtle import Turtle
from turtle import Screen

screen = Screen()
UP = 20
DOWN = 20

class bar(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.speed('fastest')
        self.goto(x,y)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    



