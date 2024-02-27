from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level =1 
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()
        self.score = 0
        self.high_score=0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font= FONT)


    def increase_level(self):
        self.level += 1 
        self.update_scoreboard()   
    
    def reset(self):
        if self.score >self.high_score:
            self.high_score =self.score
        self.score = 0
        self.update_scoreboard()    


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= FONT)
