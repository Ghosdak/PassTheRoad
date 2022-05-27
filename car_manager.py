from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.allcars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        z = randint(1,4)
        if z == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(320, randint(-250, 250))
            self.allcars.append(car)
        
    def move(self):
        for car in self.allcars:
            car.back(self.speed)
    
    def again_faster(self):
        for car in self.allcars:
            car.ht()
        self.allcars = []
        self.speed += MOVE_INCREMENT