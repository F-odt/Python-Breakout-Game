# Breakout Game 🏏

## Overview

Breakout is a classic arcade game where the player controls a paddle to bounce a ball and break bricks. 
This implementation is written in Python using the Turtle graphics library.

## How to Play

1. Run the `main.py` file to start the game.
2. Use the left and right arrow keys to move the paddle.
3. The ball will bounce off the walls, the paddle, and the bricks.
4. Break all the bricks to win the game.
5. If the ball falls below the paddle, it resets to the center.
6. Press the Escape key at any time to close the game.

## Game Elements

- **Paddle**: Controlled by the player, moves left and right at the bottom of the screen.
- **Ball**: Bounces around the screen, breaking bricks and bouncing off the paddle.
- **Bricks**: Arranged at the top of the screen in different colors. Disappear when hit by the ball.
- **Score**: Displayed in the top-left corner, increases by 10 points for each brick broken.

## Files

- `main.py`: The main game loop and initialization.
- `paddle.py`: Contains the Paddle class.
- `ball.py`: Contains the Ball class.
- `brick.py`: Contains the Brick class and setup function for bricks.
- `scoreboard.py`: Handles the score display and updates.

## Requirements

- Python 3.x
- Turtle graphics library (usually comes pre-installed with Python)

## Controls

- Left Arrow: Move paddle left
- Right Arrow: Move paddle right
- Escape: Close the game

## Customization

You can customize various aspects of the game by modifying the respective files:

- Change brick colors in `brick.py`
- Adjust ball speed in `ball.py`
- Modify paddle size in `paddle.py`
- Alter screen dimensions in `main.py`

Enjoy playing Breakout! 🎮
