from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,-50)
        self.x_move = 10
        self.y_move = 10


    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def collision_y(self):
        self.y_move *= -1

    def collision_x(self):
        self.x_move *= -1