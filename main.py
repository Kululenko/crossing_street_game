import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#Setup and objects
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()




#Movement
screen.listen()
screen.onkey(player.move_up,"Up")


#logic and rules
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.movement()
    for car in car_manager.carlist:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on=False
    if player.ycor() > 285:
        player.lv_up()
        car_manager.lv_up()
        scoreboard.lv_up()


            
screen.exitonclick()