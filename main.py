from turtle import Turtle, Screen
import random

tom = Turtle()
Screen().bgcolor("white")
tom.color(random.random(), random.random(), random.random())
direction = [0, 90, 180, 270]
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white", "gray", "brown", "cyan", "magenta",
          "lime", "navy", "maroon", "olive", "silver", "teal", "aqua", "gold", "indigo", "limegreen", "lightblue",
          "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightsteelblue",
          "lightyellow", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
          "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "navyblue",
          "olivedrab", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred",
          "papayawhip", "peachpuff", "peru", "plum", "powderblue", "rosybrown", "royalblue", "saddlebrown", "salmon",
          "sandybrown", "seagreen", "seashell", "sienna", "skyblue", "slateblue", "slategray", "snow", "springgreen",
          "steelblue", "tan", "thistle", "tomato", "turquoise", "violet", "wheat", "yellowgreen"]
tom.hideturtle()
tom.speed("fastest")
tom.width(3)


for _ in range(1200):
    tom.color(random.choice(colors))
    tom.forward(25)
    tom.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
