import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

cars = []



screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    num_cars = random.randint(7,15)
    for car in range(num_cars):
        car = CarManager()
        cars.append(car)
        time.sleep(0.3)

    for car in cars:
        car.movement()