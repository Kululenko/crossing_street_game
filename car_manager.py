from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, shape: str = "square"):
        super().__init__(shape)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(y=random.randint(-290,290),x=290)
        self.shapesize(stretch_len=2)
        self.setheading(180)
        
        

    def movement(self):
        self.forward(STARTING_MOVE_DISTANCE)
            

