# Day 86
from turtle import Turtle, Screen
from paddle import Paddle
from blocks import Block
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(delay=0)

paddle = Paddle((0, -260))
block_list = []
red_pos = -355
for i in range(8):
    block = Block((red_pos, 200), "red")
    block_list.append(block)
    red_pos +=100


blue_pos = -300
for i in range(7):
    block = Block((blue_pos, 150), "blue")
    block_list.append(block)
    blue_pos += 100

yellow_pos = -355
for i in range(8):
    block = Block((yellow_pos, 100), "yellow")
    block_list.append(block)
    yellow_pos += 100

green_pos = -300
for i in range(7):
    block = Block((green_pos, 50), "green")
    block_list.append(block)
    green_pos += 100

pink_pos = -355
for i in range(8):
    block = Block((pink_pos, 0), "pink")
    block_list.append(block)
    pink_pos += 100

brown_pos = -300
for i in range(7):
    block = Block((brown_pos, -50), "brown")
    block_list.append(block)
    brown_pos += 100



print(block_list)

ball = Ball()

screen.listen()

# functionality of the paddle
screen.onkey(key = 'Left', fun = paddle.left)
screen.onkey(key = 'Right', fun = paddle.right)

# functionality of the game
game_is_on = True
while game_is_on:
    ball.move()
    #if ball.ycor() > 280:
       # ball.bounce()
    if ball.ycor() < -240 and ball.distance(paddle) < 120:
        ball.bounce()
    elif ball.ycor() > 280:
        ball.bounce()
    elif ball.xcor() > 350 or ball.xcor() < -350:
        ball.p_bounce()
    else:
        for item in block_list:
            if ball.distance(item) < 50:
                item.hideturtle()
                block_list.remove(item)
                ball.bounce()
screen.exitonclick()