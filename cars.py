from turtle import Turtle,colormode
import random

colormode(255)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        self.setheading(180)