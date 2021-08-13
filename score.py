from turtle import Turtle, clear
from warnings import formatwarning
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.changelevel()
    
    def changelevel(self):
        self.clear()
        self.goto(-270, 240)     
        self.write(f'Level: {self.level}', align='left', font=("Courier", 30, 'normal'))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!!!', align='center', font=("Courier", 30, 'normal')) 