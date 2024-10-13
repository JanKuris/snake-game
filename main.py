from turtle import *
import time 
from game_elements.snake import  Snake
from game_elements.food import Food
from game_elements.score_board import ScoreBoard
from game_elements.menu import Menu
from const import *
 
game_run = True

# Initialize the game screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

# Create game objects
snake = Snake()
food = Food()
score_board = ScoreBoard()
menu = Menu()

# Bind key events
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(menu.play, "Return")
screen.onkey(menu.play, 'r')

def check_collisions():
     #food collision
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend_body() 
        score_board.increase_score() 
    #tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True
    #wall collision 
    if abs(snake.head.xcor()) > (SCREEN_WIDTH / 2 - 20) or abs(snake.head.ycor()) > (SCREEN_HEIGHT / 2 - 20):
        return True


def game_reset():
    while not menu.game_active:
        snake.hide_snake()
        menu.end()
        screen.update()

def start_menu_loop():
    while not menu.game_active:
            snake.hide_snake()
            menu.start()
            screen.update()

start_menu_loop()

while game_run:
    snake.show_snake()
    snake.move()
    screen.update()
    time.sleep(0.1)

    #handle collision 
    if check_collisions():
        menu.game_active = False
        game_reset() 
        snake.reset()
        food.new_food()
        score_board.high_score_check()
        score_board.reset_score()


screen.mainloop()
