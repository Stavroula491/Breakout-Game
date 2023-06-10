from turtle import Turtle

class Block(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=2, stretch_len=4)
        self.penup()
        self.goto(position)
