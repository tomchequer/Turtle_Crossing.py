from turtle import Turtle,colormode
import random

colormode(255)
move_increment = 50
move_distance = 8

class CarManager():
    def __init__(self):
        self.cars = []
        self.carspeed  = move_distance
        
    def create_car(self):
        randomchance = random.randint(1,4)
        if randomchance == 1: 
            new = Turtle()
            new.penup()
            new.shape('square')
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            new.setheading(180)
            new.startingy = random.randint(-250, 250)
            new.goto(290, new.startingy)
            self.cars.append(new)
        
    def move(self):
        for i in self.cars:    
            i.forward(move_distance)
        
    def levelup(self):
        self.carspeed += move_increment
    
    
    
    