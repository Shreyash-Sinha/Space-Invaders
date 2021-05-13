from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.goto(0, -270)
        self.velocity = 10
        self.shapesize(stretch_len=2, stretch_wid=3)

    def move_left(self):
        if self.xcor() > -380:
            self.goto(self.xcor()-self.velocity, self.ycor())

    def move_right(self):
        if self.xcor() < 380:
            self.goto(self.xcor()+self.velocity, self.ycor())