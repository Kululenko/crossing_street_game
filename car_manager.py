from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carlist = []

    def create_car(self): 
        random_int = random.randint(1,6)
        if random_int == 1:
            self.shape("square")        #bug with square?
            self.color(random.choice(COLORS))
            self.penup()
            self.goto(y=random.randint(-250,250),x=290)
            self.shapesize(stretch_len=2)
            self.setheading(180)
            self.carlist.append(self)
        
        

    def movement(self):
        for car in self.carlist:
            car.forward(STARTING_MOVE_DISTANCE)
            

