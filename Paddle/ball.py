from re import A
from turtle import Turtle
import random
class Ball:
    def __init__(self):
        self.tur=Turtle(shape="circle")
        self.tur.speed("fastest")
        self.tur.color("red")
        self.tur.penup()
        a=random.randint(30,60)
        b=180-a
        c=random.randint(0,1)
        if(c==0):
            c=a
        if(c==1):
            c=b
        self.tur.seth(c)
    def move(self):
        self.tur.forward(10)
    def bounce(self,mode):
        if(self.tur.ycor()>=290 and mode==1):
            self.tur.seth(self.tur.heading()+270)   
        if(self.tur.ycor()<=-290 and mode==1):
            self.tur.seth(self.tur.heading()+270)           
        if(mode==-1):
            self.tur.seth(self.tur.heading()+270) 
    def spawn(self):
        self.tur.goto([0,0])
        


