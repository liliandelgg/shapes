# shapes

from turtle import *
import math

# Name your Turtle.
timmy = Turtle()

# Set Up your screen and starting position.
timmy.penup()
setup(500,300)
x_pos = -250
y_pos = -150
timmy.setposition(x_pos, y_pos)


### Write your code below:
def square(steps, angle, speed):

    timmy.pendown()
    timmy.pencolor("blue")
    timmy.pensize(5)
    timmy.speed(speed)

    timmy.forward(steps)
    timmy.left(angle)
    timmy.forward(steps)
    timmy.left(angle)
    timmy.forward(steps)
    timmy.left(angle)
    timmy.forward(steps)
    timmy.left(angle)

    for i in (1,5):
        print("Good Job!")

square(500, 90, 20)


# Close window on click.
exitonclick()
