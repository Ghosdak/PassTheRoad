import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=turtle.move_fd)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    
    #detect collision with cars
    
    for car in cars.allcars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
            
    if turtle.ycor() > 280:
        score.level_up()
        turtle.start_position()
        cars.again_faster()

screen.exitonclick()