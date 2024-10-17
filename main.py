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
scoreboard = Scoreboard()

#key binding
screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")

speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    carmanager.move_cars()  # Add this line to move cars

    #Detect collision to turtle
    if carmanager.detect_player_collision(player):
        game_is_on = False
        scoreboard.game_over()
        
    elif player.ycor() > 280:
        scoreboard.point()
        player.goto(0, -280)
        speed *= 0.9
        print(speed)

screen.exitonclick()






