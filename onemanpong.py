# Simple One Man Pong in Python3
# by - Zaid Hassan
# Date - 20-Dec-22
# Time - 7:59 PM

import turtle
import time
import os
import sys
import time
import keyboard

w = turtle.Screen()
w.title("One Man Pong by @zaid-hassan")
w.bgcolor("black")
w.setup(width=800, height=600)
w.tracer(0)

# Lives
life= 5

#counter
count = 0

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.3     # d is like delta (change in x) Everytime our ball moves its gonna move by 0.3 px
ball.dy = -0.3     # d is like delta (change in y) combining x = 2 and y = 2 it will move diagonally

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(315, 250)
pen.write("lives: 5", align="center", font=("Courier", 20, "normal"))

# Title
title = turtle.Turtle()
title.speed(0)
title.color("grey")
title.penup()
title.hideturtle()
title.goto(0, 240)
title.write("One Man Pong", align="center", font=("Courier", 30, "bold"))


# Counter
pen_c = turtle.Turtle()
pen_c.speed(0)
pen_c.color("grey")
pen_c.penup()
pen_c.hideturtle()
pen_c.goto(-300, 250)
pen_c.write("counter: 0", align="center", font=("Courier", 20, "normal"))

# Instructions
inst = turtle.Turtle()
inst.speed(0)
inst.color("grey")
inst.penup()
inst.hideturtle()
inst.goto(0, 230)
inst.write("Use <- Left and right -> arrow keys to play, Esc to exit and space to restart", align="center", font=("Courier", 8, "bold"))

# Function 
# ---------------------movements---------------------

# ................Left-Right................
def paddle_left():
    x = paddle.xcor()   # .xcor() method is from the turtle module, it returns the x coordinate
    x -= 20             # .xcor get the x coordinates then increase them by 20 and then .setx to the new x coordinate
    paddle.setx(x)
    if x < -350:
        paddle.setx(-350)

def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)
    if x > 350:
        paddle.setx(350)

def close():
    turtle.bye()

def res():
    time.sleep(1)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Keyboard Binding
w.listen()  # In the turtle module we need to do <windowname>.listen | This will tell it to listen for keyboard input
w.onkeypress(paddle_left, "Left")  # whats happening here is w.listen tells to listen to the keyboard, and if the keypress is "left" (.onkeypress) then call the function paddle_left
w.onkeypress(paddle_right, "Right")

w.listen()
w.onkeypress(close, "Escape")

w.listen()
w.onkeypress(res, "space")

time.sleep(.6)
# Main Game
while True:
    w.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking 
    # .............Top.............
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # .............Bottom.............
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        life -= 1
        pen.clear()
        pen.write("Lives: {}".format(life), align="center", font=("Courier", 20, "normal"))
    # .............Right.............
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    # .............Left.............
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Paddle and ball collision
    if ball.ycor() <= -240 and ball.ycor() > -250 and (ball.xcor() < paddle.xcor() + 42 and ball.xcor() > paddle.xcor() -42):
        ball.sety(-240)
        ball.dy *= -1
        count += 1
        pen_c.clear()
        pen_c.write("counter: {}".format(count), align="center", font=("Courier", 20, "normal"))

    # game ending
    if life == 0:
        pen_c.clear()
        pen.clear()
        pen.color("white")
        pen.goto(0, 0)
        pen.write("Game Over", align="center", font=("Carrier", 30, "normal"))
        pen_c.color("grey")
        pen_c.goto(0, -45)
        pen_c.write("Score: {}".format(count), align="center", font=("Carrier", 30, "normal"))
        turtle.done()
        break