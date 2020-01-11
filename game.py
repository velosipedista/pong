# import math
import turtle
import os

wn = turtle.Screen()
wn.title("gAnZ's PoNg")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# score
score_hilka_1 = 0
score_hilka_2 = 0

# hilka 1
hilka_1 = turtle.Turtle()
hilka_1.speed(0)
hilka_1.shape("square")
hilka_1.color("white")
hilka_1.shapesize(stretch_wid=5,stretch_len=1)
hilka_1.penup()
hilka_1.goto(-350,0)

# hilka 2
hilka_2 = turtle.Turtle()
hilka_2.speed(0)
hilka_2.shape("square")
hilka_2.color("white")
hilka_2.shapesize(stretch_wid=5,stretch_len=1)
hilka_2.penup()
hilka_2.goto(350,0)

# topche
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = -0.3

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"player 1: {score_hilka_1} player 2: {score_hilka_2}", align="center",font=("Courier",20, "bold"))


def hilka_1_up():
    y = hilka_1.ycor()
    y += 20
    hilka_1.sety(y)


def hilka_1_down():
    y = hilka_1.ycor()
    y -= 20
    hilka_1.sety(y)


def hilka_2_up():
    y = hilka_2.ycor()
    y += 20
    hilka_2.sety(y)


def hilka_2_down():
    y = hilka_2.ycor()
    y -= 20
    hilka_2.sety(y)




# keyboard binding
wn.listen()
wn.onkeypress(hilka_1_up,"a")
wn.onkeypress(hilka_1_down,"z")
wn.onkeypress(hilka_2_up,"k")
wn.onkeypress(hilka_2_down,"m")

# main game loop

while True:
    wn.update()
# move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
# borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # os.system("aplay bounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_hilka_1 += 1
        pen.clear()
        pen.write(f"player 1: {score_hilka_1} player 2: {score_hilka_2}", align="center", font=("Courier", 20, "bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_hilka_2 += 1
        pen.clear()
        pen.write(f"player 1: {score_hilka_1} player 2: {score_hilka_2}", align="center", font=("Courier", 20, "bold"))
# otskok
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < hilka_2.ycor() + 40 and ball.ycor() > hilka_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce_hilka.wav&")
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
            (ball.ycor() < hilka_1.ycor() + 40 and ball.ycor() > hilka_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce_hilka.wav&")
