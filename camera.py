import turtle
from random import randint
import time

screen = turtle.Screen()  # графическое окно

pen = turtle.Turtle()     # графический объект
pen.speed(0)


def square(
    x: int, y: int,
    width: int,
    line_color="black",
    thickness=1
):
    pen.color(line_color)
    pen.width(thickness)
    pen.up()
    pen.goto(x - width // 2, y )
    pen.down()
    i = 4             # нарисовать фигуру
    while i > 0:
        pen.fd(width)
        pen.lt(90)
        i -= 1
    pen.ht()


leo = turtle.Turtle()
leo.speed(0)
leo.shape("turtle")
leo.color("blue")
leo.up()
leo.goto(0, 0)

raph = turtle.Turtle()
raph.speed(0)
raph.shape("turtle")
raph.color("red")
raph.up()
raph.goto(0, 0)

don = turtle.Turtle()
don.speed(0)
don.shape("turtle")
don.color("purple")
don.up()
don.goto(0, 0)

mike = turtle.Turtle()
mike.speed(0)
mike.shape("turtle")
mike.color("orange")
mike.up()
mike.goto(0, 0)
leo.lt(randint(1, 360))
raph.lt(randint(1, 360))
don.lt(randint(1, 360))
mike.lt(randint(1, 360))

square(0, -100, 200, 'black', 2)

while True:
    leo.fd(randint(1, 5))
    raph.fd(randint(1, 5))
    don.fd(randint(1, 5))
    mike.fd(randint(1, 5))
    if abs(leo.xcor()) > 100 or abs(raph.xcor()) > 100 or abs(don.xcor()) > 100 or abs(mike.xcor()) > 100:
        break
    elif abs(leo.ycor()) > 100 or abs(raph.ycor()) > 100 or abs(don.ycor()) > 100 or abs(mike.ycor()) > 100:
        break

time.sleep(2)

if leo.xcor() > 100 or leo.ycor() > 100:
    leo.goto(0, 200)
    leo.seth(90)
elif raph.xcor() > 100 or raph.ycor() > 100:
    raph.goto(0, 200)
    raph.seth(90)
elif don.xcor() > 100 or don.ycor() > 100:
    don.goto(0, 200)
    don.seth(90)
elif mike.xcor() > 100 or mike.ycor() > 100:
    mike.goto(0, 200)
    mike.seth(90)

screen.mainloop()
