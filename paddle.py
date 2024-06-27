import turtle as jay


class Paddle(jay.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        x = self.xcor() - 20
        if x > -350:
            self.setx(x)

    def move_right(self):
        x = self.xcor() + 20
        if x < 350:
            self.setx(x)
