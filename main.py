from turtle import Turtle, Screen
from cars import Car
from player import Player
#from score import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

gameison = True

player_turtle = Player()

screen.listen()
screen.onkey(player_turtle.walk, "Up")

testcar = Car()

while gameison:
    time.sleep(0.1)
    screen.update()
    


screen.exitonclick()