from turtle import *
import time 
from game_elements.snake import  Snake
from game_elements.food import Food
from game_elements.score_board import ScoreBoard
from game_elements.menu import Menu
from const import *

game_run = True
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score_board = ScoreBoard()
menu = Menu()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
start_key = screen.onkey(menu.enter, "Return")

while not menu.game_active:
    snake.hide_body()
    menu.start()
    screen.update()
    
while game_run:
    snake.show_snake()
    snake.move()
    screen.update()
    time.sleep(0.1)
    #food colision
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend_body() 
        score_board.increase_score() 
    #colision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score_board.end_round()
    #wall colision 
    if abs(snake.head.xcor()) > 380 or abs(snake.head.ycor()) > 380:
        score_board.end_round()
        snake.reset()
screen.mainloop()
