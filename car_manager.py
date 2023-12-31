import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            self.hideturtle()
            new_car=Turtle("square")

            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y=random.randint(-250,250)
            new_car.goto(300,rand_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for cr in self.all_cars:
            cr.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT










