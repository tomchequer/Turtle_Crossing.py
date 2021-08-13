from turtle import Turtle, Screen, distance
from car_manager import CarManager
from player import Player
from score import Score
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

gameison = True

player_turtle = Player()

car_manager = CarManager()

score = Score()

screen.listen()
screen.onkey(player_turtle.walk, "Up")

        

while gameison:
    time.sleep(0.1)
    screen.update()    
    car_manager.create_car()
    car_manager.move()
    
    #detecting colision with cars
    for i in car_manager.cars:
        if player_turtle.distance(i) < 20:
            score.game_over()
            gameison = False
    
    #detect player won
    if player_turtle.ycor() > 295:
        player_turtle.gotostart()
        score.level += 1
        score.changelevel()

    
screen.exitonclick()