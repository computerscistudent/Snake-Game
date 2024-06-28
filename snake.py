from turtle import Turtle
starting_positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0
class SNAKE:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for p in starting_positions:
            self.add_segment(p)
    def add_segment(self ,p):
        new_segment = Turtle()
        new_segment.color("red")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(p)
        self.segments.append(new_segment)
    def ext_snake(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for s in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[s - 1].xcor()
            newy = self.segments[s - 1].ycor()
            self.segments[s].goto(newx, newy)
        self.head.forward(move_distance)

    def up(self):
        if self.head.setheading != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.setheading != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.setheading != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.setheading != Left:
            self.head.setheading(Right)