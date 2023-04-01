from turtle import Turtle
class cur:
    def __init__(self,x):
        self.pa=Turtle(shape="square")
        self.pa.color("white")
        self.pa.shapesize(stretch_len=5,stretch_wid=1)
        self.pa.setheading(90)
        self.pa.penup()
        self.pa.goto([x,0])
    def up(self):
        if(self.pa.ycor()<200):
            self.pa.forward(40)
    def down(self):
        if(self.pa.ycor()>-200):
            self.pa.backward(40)

        
