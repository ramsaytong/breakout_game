from turtle import Turtle
import random
x = (-350,350)
y = (0,300)



row = 3
colum = 3
WINDOWSCOPE = (800, 600)


COLOR = ["red","yellow","purple","green","orange","blue","gold","pink"]

class Block(Turtle):
    def __init__(self,posistion):
        super().__init__()
        self.block_creat(posistion)



    def block_creat(self,posistion):
        self.penup()
        self.shape("square")
        self.color(random.choice(COLOR))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(posistion)



