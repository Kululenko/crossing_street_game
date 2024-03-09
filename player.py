from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "turtle"):
        super().__init__(shape)
        self.color("black")
        self.penup()
        self.goto(y=-280,x=0)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)


    def lv_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(y=-280,x=0)