from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [350, 325, 300, 275, 250, 225]
random_cars = []


class CarManager(Turtle):
      def __init__(self):
        super().__init__()
        self.penup()
        
      def install_cars(self):
        for traffic_cars in range(0, 6):
           new_car = self.shape("square")
           self.color(COLORS[traffic_cars])
           self.goto(x=0, y=POSITIONS[traffic_cars])
           random_cars.append(new_car)
    
