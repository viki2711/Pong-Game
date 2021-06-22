from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
DOWN = 270
START_X = 0
START_Y = 260
STEP = 20


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.set_up()
        self.create_divider()

    def set_up(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(START_X, START_Y)
        self.pendown()
        self.pensize(2)
        self.setheading(DOWN)

    def create_divider(self):
        for i in range(int(START_Y/STEP)):
            self.forward(STEP)
            self.penup()
            self.forward(STEP)
            self.pendown()