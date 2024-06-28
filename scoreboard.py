from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_sb()



    def update_sb(self):
        self.write(f"SCORE:{self.score}", align="center", font=("ariel", 24, "italic"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("ariel", 24, "italic"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_sb()

