from turtle import Turtle

my_font = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=my_font)
        self.goto(0, 200)
        self.write(":", align="center", font=my_font)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=my_font)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def winner(self):
        if self.l_score > self.r_score:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=my_font)
        self.goto(0, -50)
        self.write(f"{self.winner()}", align="center", font=("Courier", 30, "normal"))
