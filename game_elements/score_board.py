from turtle import * 
from const import *
import os

class ScoreBoard(Turtle):
   
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('black')
        self.score_value = 0
        self.high_score_value = self.load_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.display_score(f"Score:{self.score_value}", -100, SCREEN_WIDTH - 450)
        self.display_score(f"High Score: {self.high_score_value}", 80, SCREEN_WIDTH - 450) 

    def display_score(self, text, x, y):
        self.goto(x,y)
        self.write(text, align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score_value += 1
        self.update_scoreboard()
        

    def load_high_score(self):
        try:

            if os.path.exists("high_score.txt"):
                with open("high_score.txt", "r") as file:
                    return int(file.read())
            else:
                return 0
        except(ValueError, IOError):
            return 0 # If file is empty or corrupt, set high score to 0
            
    def save_high_score(self, new_high_score):
        with open("high_score.txt", "w") as file:
            file.write(str(new_high_score))
    
    def high_score_check (self):
        if self.score_value > self.high_score_value:
            self.high_score_value = self.score_value
            self.save_high_score(self.high_score_value) 
    
    def reset_score(self):
        self.score_value = 0
        self.update_scoreboard()