from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.color("blue")
        self.shape("turtle") 
        self.penup()
        self.goto(STARTING_POSITION)
        self.tilt(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_right(self):
        right_d = self.xcor() + MOVE_DISTANCE
        self.goto(right_d, self.ycor())

    def move_left(self):
        left_a = self.xcor() - MOVE_DISTANCE
        self.goto(left_a, self.ycor())
  
        
    
