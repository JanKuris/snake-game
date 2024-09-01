from turtle import * 
from const import SCREEN_WIDTH, SCREEN_HEIGHT
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
        self.goto(-100, SCREEN_WIDTH - 450)
        self.write(f"Score:{self.score_value}", align= ALIGMENT, font=FONT)
        self.goto(80, SCREEN_WIDTH - 450)
        self.write(f"High Score: {self.high_score_value}", align= ALIGMENT, font=FONT)

    def increase_score(self):
        self.score_value += 1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        if self.score_value > self.high_score_value:
            self.high_score_value = self.score_value
            self.save_high_score(self.high_score_value) 
        self.goto(0, 0)
        self.write("YOU FAIL", align= ALIGMENT, font=FONT)
        

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                return int(file.read())
        else:
            return 0
        
    def save_high_score(self, new_high_score):
        with open("high_score.txt", "w") as file:
            file.write(str(new_high_score))
    