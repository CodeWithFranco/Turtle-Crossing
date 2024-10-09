from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [-250, -150, -50, 50, 150, 250]

player = Player()

class CarManager:
    def __init__(self):
        self.cars = []

    def install_cars(self):
        for turtle_number in range(0, 6):
            new_car = Turtle(shape = "square")
            new_car.penup()
            new_car.color(COLORS[turtle_number])
            new_car.goto(random.randint(300, 600), POSITIONS[turtle_number])  # Position outside the screen
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
    
    def playerHitCar(self):
        if player 
