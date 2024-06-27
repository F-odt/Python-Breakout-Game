import turtle as jay
from paddle import Paddle
from ball import Ball
from brick import setup_bricks
from scoreboard import ScoreBoard

# Set up the screen
screen = jay.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Breakout Game🏏')
screen.tracer(0)

# Create game objects
paddle = Paddle()
ball = Ball(paddle)
bricks = setup_bricks()
score_board = ScoreBoard()

# Set up controls
screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')

# Main game loop
running = True


def close_game():
    global running
    running = False
    screen.bye()


screen.onkey(close_game, "Escape")

while running:
    screen.update()
    ball.move()

    # Collision detection for bricks
    for brick in bricks:
        if ball.distance(brick) < 27:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move brick off-screen
            bricks.remove(brick)
            score_board.increase_score()
            break

    # Check for win condition
    if not bricks:
        ball.reset()
        screen.update()
        # Implement win logic here (e.g., display win message, reset game, etc.)
        break

    jay.update()

jay.done()
