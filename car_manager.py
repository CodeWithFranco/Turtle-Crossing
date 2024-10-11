from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [-250, -150, -50, 50, 150, 250]

class CarManager:
    def __init__(self):
        self.cars = []  # Create a list to store all cars
        self.car_creation_timer = random.randint(20, 50)  # Random interval for car creation

    def install_cars(self):
        # Add a new car to the list
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make the car wider
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(270, random.choice(POSITIONS))  # Start from the right edge of the screen
        self.cars.append(new_car)  # Store the car in the list

    def create_car_with_intervals(self):
        # Decrease timer
        self.car_creation_timer -= 1

        # Create a new car if the timer reaches zero, then reset the timer
        if self.car_creation_timer <= 0:
            self.install_cars()
            # Reset the timer to a new random value, creating random intervals between cars
            self.car_creation_timer = random.randint(20, 50)

    def move_cars(self):
        # Move all cars in the list
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def playerHitCar(self):
        pass
