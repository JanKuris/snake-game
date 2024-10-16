from turtle import *
from const import *


class Snake():
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]
        
    def create_body(self):
        for position in STARTING_POSITIONS:         
            self.add_segment(position)

    def hide_snake(self):
        for segment in self.segments:
            segment.hideturtle()

    def show_snake(self):
        for segment in self.segments:
            segment.showturtle()

            
    def add_segment(self, position):
        new_segment = Turtle(SNAKE_SHAPE)
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_body(self):
        self.add_segment(self.segments[-1].position())
       
    def move(self):
        for seg_number in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:  
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_body()
        self.head = self.segments[0]