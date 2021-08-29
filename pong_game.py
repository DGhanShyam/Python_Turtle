import turtle

from turtle import Turtle
from turtle import Screen

from random import *


scrn = Screen()



scrn.title("Pong game 🎉 🏓")
scrn.setup(width=1000, height=600)
scrn.colormode(255)
scrn.bgcolor(51, 0, 25)


# changing variables
speed= 0



# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=5, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
 
 
# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=5, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
 
 
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5



left_player = 0
right_player = 0

 
# Displays the score
display = turtle.Turtle()
display.speed(0)
display.color("white")
display.penup()
display.hideturtle()
display.goto(-400, 260)

display.goto(350, 260)
display.write(" Press enter to start: ",
             align="center", font=("Courier", 14, "normal"))

display.goto(350, 230)
display.write("CONTROLS: up, down , w, z",
             align="center", font=("Courier", 12, "normal"))


sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(-350, 260)
sketch.write("SCORE - LEFT : 0  RIGHT: 0",
             align="center", font=("Courier", 12, "normal"))


# Functions to move paddle vertically
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


def runGame():
    left_player = 0
    right_player = 0
 
    while True:
        scrn.update()

 
        hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
        hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

        # Checking borders
        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1
 
        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1
 
        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            left_player += 1
            sketch.clear()
            # sketch.goto(-350, 260)
            sketch.write("SCORE- LEFT : {}    RIGHT: {}".format(
                      left_player, right_player),align="center",
                      font=("Courier", 12, "normal"))

             
        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            right_player += 1
            sketch.clear()
            # sketch.goto(-350, 260)            
            sketch.write("SCORE- LEFT : {}    RIGHT: {}".format(
                                 left_player, right_player),align="center",
                                 font=("Courier", 12, "normal"))
 
    # Paddle ball collision
        if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40):
            hit_ball.setx(360)
            hit_ball.dx*=-1
            color=['red', 'blue', 'green', 'pink', 'yellow']
            speed=[30, 40, 50]
            
            x = sample(color,  1)   
            y= sample(speed, 1)
            hit_ball.color(x[0])
            left_pad.color(x[0])
            hit_ball.speed(y[0])

        if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+40 and hit_ball.ycor()>left_pad.ycor()-40):
            hit_ball.setx(-360)
            hit_ball.dx*=-1
            color=['red', 'blue', 'green', 'pink', 'yellow']
            speed=[30, 40, 50, 60]
            
            x = sample(color,  1)   
            y= sample(speed, 1)  
            hit_ball.color(x[0])
            right_pad.color(x[0])
            hit_ball.speed(y[0])
            

scrn.listen()
scrn.onkeypress(runGame, "Return")
scrn.onkeypress(paddleaup, "w")
scrn.onkeypress(paddleadown, "z")
scrn.onkeypress(paddlebup, "Up")
scrn.onkeypress(paddlebdown, "Down")

win = turtle.Screen()
win.mainloop()
# scrn.exitonclick()
