from turtle import * 
from const import SCREEN_WIDTH, SCREEN_HEIGHT
from const import *

class ScoreBoard(Turtle):
   
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('black')
        self.goto(SCREEN_HEIGHT // 3, SCREEN_WIDTH // 2.5)
        self.score_value = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score:{self.score_value}", align= ALIGMENT, font=FONT)

    def increase_score(self):
        self.score_value += 1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGMENT, font=FONT)
