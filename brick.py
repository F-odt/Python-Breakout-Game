import turtle as jay

class Brick(jay.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x, y)

def setup_bricks():
    brick_colors = ['red', 'orange', 'yellow', 'green', 'blue']
    bricks = []
    for i in range(-350, 400, 75):
        for j in range(250, 150, -25):
            color_index = (j // 25) % len(brick_colors)
            brick = Brick(i, j, brick_colors[color_index])
            bricks.append(brick)
    return bricks