from turtle import Turtle

POSISTION = (0,-250)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_creat()


    def paddle_creat(self):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(POSISTION)


    def paddle_left(self):
        new_x = self.xcor() - 10
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def paddle_right(self):
        new_x = self.xcor() + 10
        new_y = self.ycor()
        self.goto(new_x, new_y)