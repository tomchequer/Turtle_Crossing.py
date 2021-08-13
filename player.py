from turtle import Turtle
#constants?

SPAWNPOINT = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(SPAWNPOINT)
        
    
    def walk(self):
        newy = self.ycor() + 20
        self.goto(0, newy)
        