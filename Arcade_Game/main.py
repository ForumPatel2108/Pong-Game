
import turtle
from turtle import Turtle
from turtle import Screen
from bar_move import bar 
from ball import balls
import time
from scoreboard import ScoreBoard
 
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
scoreboard = ScoreBoard()

left_paddle = bar(-350,0)
right_paddle = bar(350,0)
ball1 = balls()

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

game = Turtle()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball1.move_speed)
    ball1.move()
    if ball1.ycor() < -280 or ball1.ycor() > 280:
        ball1.bounce_y()

    if ball1.distance(right_paddle) < 50 and ball1.xcor() > 320 or ball1.distance(left_paddle) < 50 and ball1.xcor() < -320:
        ball1.bounce_x()

    # l paddle misses
    if ball1.xcor() < -380:
        ball1.ball_reset()
        scoreboard.r_point()

    # r paddle misses
    if ball1.xcor() > 380:
        ball1.ball_reset()
        scoreboard.l_point()

screen.exitonclick()