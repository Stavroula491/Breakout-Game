from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.penup()
        self.goto(position)
    # deksia
    def right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())