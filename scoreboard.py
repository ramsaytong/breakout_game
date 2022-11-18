from turtle import  Turtle
ALIGN = 'center'
FONT = ('Arial', 20, 'normal')
POSITION = (0, 270)




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_update()

    def score_update(self):
            self.clear()
            self.score += 1
            self.goto(POSITION)
            self.write(f"Score：{self.score -1} ", align= ALIGN , font=FONT)


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Your final Score：{self.score - 1} ", align=ALIGN, font=('Arial', 50, 'normal'))