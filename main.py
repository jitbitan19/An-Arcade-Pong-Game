# TODO 1: Create the Screen
# TODO 2: Create and move a paddle
# TODO 3: Create another Paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep Score


from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game_point = 5
screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
scoreboard = Scoreboard()
screen.update()
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        # print("Made Contact")
        ball.bounce_x()
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()  # Add a point to left player
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()  # Add a point to right player

    if scoreboard.l_score == game_point or scoreboard.r_score == game_point:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
