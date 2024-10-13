from turtle import *
import random
from const import *

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color(FOOD_COLOR)
        self.speed(FOOD_RENDERING)
        self.new_food()

    def new_food(self):
        random_x = random.randint(-SCREEN_WIDTH//2 +20, SCREEN_HEIGHT//2 - 20)
        random_y = random.randint(-SCREEN_WIDTH//2 +20, SCREEN_HEIGHT//2 - 50)
        self.goto(random_x, random_y)
    

   


