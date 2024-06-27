import turtle as jay

class ScoreBoard(jay.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-380, 270)
        self.hideturtle()
        self.update_display()

    def increase_score(self):
        self.score += 10
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Score: {self.score}", align='left', font=('Arial', 16, 'normal'))