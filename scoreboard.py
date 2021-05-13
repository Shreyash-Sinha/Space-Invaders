from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')

    def create_scoreboard(self, score):
        """Refreshes the scoreboard"""
        self.clear()
        self.goto(250, -100)
        self.write(f"Score: {score}", align='center', font=('Courier', 30, 'normal'))


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')

    def create_scoreboard(self, lives):
        """Refreshes the scoreboard"""
        self.clear()
        self.goto(290, -200)
        self.write(f"Lives: {lives}", align='center', font=('Courier', '30', 'normal'))


class Lose(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')

    def create_scoreboard(self):
        """Refreshes the scoreboard"""
        self.clear()
        self.goto(0, 0)
        self.write(f"Your Lost against the Enemies", align='center', font=('Courier', 30, 'normal'))