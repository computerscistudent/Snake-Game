from turtle import Turtle
import random


class FOOD(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        para_x = random.randint(-280, 280)
        para_y = random.randint(-280, 280)
        self.goto(para_x, para_y)


