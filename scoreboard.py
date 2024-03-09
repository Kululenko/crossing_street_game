from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
GAMEOVERFONT = ("Courier",40,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-285,y=265)
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.write(arg=f"LEVEL: {self.level}",font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(x=-35,y=0)
        self.write(arg="GAME OVER",align="center",font=GAMEOVERFONT)