STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.color("white")
        self.shape("turtle") 
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        go_up = self.ycor() + MOVE_DISTANCE
        self.goto(0, go_up)
    
