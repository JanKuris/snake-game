from turtle import *
import random
from const import *

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-SCREEN_WIDTH//2 +20, SCREEN_HEIGHT//2 - 20)
        random_y = random.randint(-SCREEN_WIDTH//2 +20, SCREEN_HEIGHT//2 - 20)
        self.goto(random_x, random_y)

# SPECIAL FOOD == make spec. food one per 10 round. this food get 10 point value  
   