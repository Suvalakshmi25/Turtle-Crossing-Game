import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars=CarManager()
scoreboard=Scoreboard()

player=Player()
game_is_on = True

screen.listen()
screen.onkey(player.move,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_car()
    for car in cars.all_cars:
        if car.distance(player)<22:
            game_is_on=False
            scoreboard.game_over()
    if player.is_at_finish():
        player.goto_start()
        cars.level_up()
        scoreboard.increase_level()

        


screen.exitonclick()

