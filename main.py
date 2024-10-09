import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()

#key binding
screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")



game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()
    carmanager.install_cars()
    carmanager.move_cars()  # Add this line to move cars



screen.exitonclick()

