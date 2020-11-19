from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("classic")
tom.color("blue")
tom.speed("fastest")
tom.width(14)


def change_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    tom.color(red, green, blue)


# random walk
def move_right():
    change_color()
    tom.right(90)
    tom.forward(30)


def move_left():
    change_color()
    tom.left(90)
    tom.forward(30)


def move_forward():
    change_color()
    tom.forward(30)


def move_backward():
    change_color()
    tom.backward(30)


walking = [move_left, move_right, move_forward, move_backward]


def random_walk():
    random.choice(walking)()


for _ in range(500):
    random_walk()


screen = Screen()
screen.exitonclick()
