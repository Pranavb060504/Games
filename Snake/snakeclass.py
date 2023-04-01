from turtle import Turtle
from foodclass import Food
import math
class Snake:
    def __init__(self,length):
        self.tur=[]
        self.create(length)
        self.f=Food()
        self.alive=True
    def create(self,length):
            for i in range(length):
                tim=Turtle(shape="square")
                tim.color("white")
                tim.penup()
                tim.speed("slowest")
                tim.goto([-20*i,0])
                self.tur.append(tim)
    def move(self):
        if(math.sqrt((self.f.tur.xcor()-self.tur[0].xcor())**2+(self.f.tur.ycor()-self.tur[0].ycor())**2)<=12):
            self.f.spawn()
            self.f.score()
        for num in range(len(self.tur)-1,0,-1):
            nx=self.tur[num-1].xcor()
            ny=self.tur[num-1].ycor()
            self.tur[num].goto([nx,ny])
        self.tur[0].forward(20)
        if(self.tur[0].xcor()>295 or self.tur[0].xcor()<-295 or self.tur[0].ycor()>295 or self.tur[0].ycor()<-295):
            self.alive=False
    def up(self):
        if(self.tur[0].heading()!=270):
            self.tur[0].setheading(90)
    def down(self):
        if(self.tur[0].heading()!=90):
            self.tur[0].setheading(270)
    def left(self):
        if(self.tur[0].heading()!=0):
            self.tur[0].setheading(180)
    def right(self):
        if(self.tur[0].heading()!=180):
            self.tur[0].setheading(0)