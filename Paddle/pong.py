from paddle import cur
from turtle import Turtle,Screen
from ball import Ball
import time
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1=0
        self.p2=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.p1,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.p2,align="center",font=("Courier",80,"normal"))
score=scoreboard()
screen=Screen()
screen.setup(height=600,width=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("PONG")
pad1=cur(350)
pad2=cur(-350)
screen.update()
screen.listen()
screen.onkey(fun=pad1.up,key="Up")
screen.onkey(fun=pad1.down,key="Down")
screen.onkey(fun=pad2.up,key="w")
screen.onkey(fun=pad2.down,key="s")
game_on=True
cir=Ball()
while game_on==True:
    time.sleep(0.05)
    screen.update()
    cir.move()
    if((cir.tur.xcor()>=335 or cir.tur.xcor()<=-335) and ((pad1.pa.ycor()-50<cir.tur.ycor()<pad1.pa.ycor()+50)or(pad2.pa.ycor()-50<cir.tur.ycor()<pad2.pa.ycor()+50))):
        cir.bounce(-1)
    else:
        cir.bounce(1)
    if(cir.tur.xcor()>390):
        score.p1+=1
        cir.spawn()
        time.sleep(1)
    if(cir.tur.xcor()<-390):
        score.p2+=1
        cir.spawn()
        time.sleep(1)
    if(score.p1>=5 or score.p2>=5):
        game_on=False
        if(score.p1==5):
            print("P1 Wins!")
        if(score.p2==5):
            print("P2 Wins!")      
screen.exitonclick()