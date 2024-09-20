from turtle import *
from const import ALIGMENT, FONT

class Menu(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('black')    
        self.game_active = False    

    def enter(self):
        self.clear()
        self.game_active = True
        return self.game
        

    def start(self):
        if self.game_active == False: 
            self.write("For start press 'Enter'", align= ALIGMENT, font=FONT)
            

