from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-220,260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level: {self.level}",align="center",  font=FONT)
        self.level +=1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align="center",  font=FONT)