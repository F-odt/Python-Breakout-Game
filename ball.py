import turtle as jay

class Ball(jay.Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.dx = 1.5
        self.dy = 1.5
        self.paddle = paddle

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # Bounce off the walls
        if self.xcor() > 390 or self.xcor() < -390:
            self.dx *= -1
        if self.ycor() > 290:
            self.dy *= -1

        # Bounce off the paddle
        if self.ycor() < -240 and self.ycor() > -250 and (
                self.xcor() > self.paddle.xcor() - 50 and self.xcor() < self.paddle.xcor() + 50):
            self.dy *= -1

        # Check for loss
        if self.ycor() < -290:
            self.reset()

    def reset(self):
        self.goto(0, 0)
        self.dy *= -1