from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-10, 270)
        self.update()
    def update(self):
        self.clear()
        self.write(f"Level:{self.score}", align='center',font=(FONT))

    def l_point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center',font=(FONT))

