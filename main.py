from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import  Ball
from block import Block
from scoreboard import  Scoreboard
import time

#-----------------posistion set-------------------------------#
row = 5
colum = 5

POSISTION = []
x= []
x_space = 800/colum
y_space = 300/row

x = [-350 + x_space*i for i in range(0,colum)]
y = [y_space*i for i in range(0,row)]

POSISTION = [(x[j],y[i]) for i in range(0,len(y)) for j in range(0,len(x))]


#------------------------------------------------#


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Breakout Game")

screen.tracer(0)

paddle = Paddle()
ball = Ball()

block_list = []
for i in range(0,len(POSISTION)):
    block =Block(POSISTION[i])
    block_list.append(block)
print(len(block_list))
scoreboard = Scoreboard()




screen.listen()
screen.onkey(paddle.paddle_left, "Left")
screen.onkey(paddle.paddle_right, "Right")

screen_time = 0.1
game_is_on = True
while game_is_on:
    ball.movement()
    screen.update()
    time.sleep(screen_time)
###############border check#################
    for x in range(-400, 400):
        up_wall = (x, 290)
        down_wall = (x, -290)
        if ball.distance(up_wall) < 20:
            ball.collision_y()
        elif ball.distance(down_wall) < 20:
            game_is_on =False
            scoreboard.game_over()



    for y in range(-300, 300):
        right_wall = (390, y)
        left_wall = (-390, y)
        if ball.distance(right_wall) < 20 or ball.distance(left_wall) < 20:
            ball.collision_x()

############################################
    for block_piece in block_list:
        if block_piece.distance(ball) < 30:
            block_x = POSISTION[block_list.index(block_piece)][0]
            block_y = POSISTION[block_list.index(block_piece)][0]
            if 18 < abs(ball.xcor() - int(block_x)) < 30 :
                ball.collision_x()
            else:
                ball.collision_y()
            scoreboard.score_update()
            block_piece.hideturtle()
            block_list.remove(block_piece)




    if ball.distance(paddle) < 30 :
        ball.collision_y()


screen.exitonclick()