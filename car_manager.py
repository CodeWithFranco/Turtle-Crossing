from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [-250, -175, -100, -25, 50, 125, 200, 250]  # The range for vertical positioning of cars

class CarManager:
    def __init__(self):
        self.cars = []  # Create a list to store all cars

    def install_cars(self):
        # Add a new car to the list
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make the car wider
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.choice(POSITIONS))  # Start from further right edge of the screen
        self.cars.append(new_car)  # Store the car in the list

    def move_cars(self):
        # Move all cars and check if the last car is fully visible
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

        # Install a new car only if the last car is sufficiently forward
        if not self.cars or self.cars[-1].xcor() < 255:  # Check the last car's position
            self.install_cars()

    def playerHitCar(self):
        pass
