from turtle import Turtle, Screen
import random

tom = Turtle()
# Screen().bgcolor("black")
Screen().bgcolor("white")
direction = [0, 90, 180, 270]
tom.hideturtle()
tom.speed("fast")
tom.width(3)

for _ in range(1200):
    tom.color(random.random(), random.random(), random.random())
    tom.forward(25)
    tom.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
