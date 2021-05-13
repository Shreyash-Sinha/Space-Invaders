from turtle import Turtle
import random


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setheading(270)
        self.penup()
        self.goto(random.randint(-380, 380), 280)
        self.velocity = 0.03
        self.move = random.choice(['right', 'left'])
        self.shapesize(stretch_len=2, stretch_wid=2)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-self.velocity)