from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.carlist = []

    def create_car(self):     #wenn self statt new_car verwendet wird mache ich dann daraus ein Singleton? hatte ein komischen Bug wo die autos nicht kamen. Nur einer zur Zeit 
        random_int = random.randint(1,6)
        if random_int == 1:
            new_car = Turtle("square")        
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(y=random.randint(-250,250),x=300)
            new_car.shapesize(stretch_len=2)
            new_car.setheading(180)
            self.carlist.append(new_car)
        
        

    def movement(self):
        for car in self.carlist:
            car.forward(STARTING_MOVE_DISTANCE)
            

    def lv_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.movement()