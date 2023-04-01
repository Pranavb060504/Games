from turtle import Turtle
import random
class Food:
    def __init__(self):
        self.count=0
        self.tur=Turtle(shape="circle")
        self.tur.speed("fastest")
        self.tur.color("red")
        self.tur.penup()
        self.tur.shapesize(stretch_len=0.5,stretch_wid=0.5)
    def spawn(self):
        xco=random.randint(-275,275)
        yco=random.randint(-275,275)
        self.tur.goto(xco,yco)
    def score(self):
        self.count+=1
        
