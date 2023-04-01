from turtle import Turtle,Screen
import random
a=0
def move_forward(tim):
    tim.forward(random.randint(1,10))
color=["violet","blue","green","yellow","orange","red"]
allturtles=[]
screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="Make your bet",prompt="Enter color:")
for i in range(6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(f"{color[i]}")
    tim.goto([-230,100-20*i])
    allturtles.append(tim)
j=0
while(a==0):
    for tur in allturtles:
        move_forward(tur)
        if(tur.xcor()>230):
            a=1
for i in range(6):
    if(allturtles[i].xcor()>230):
        j=i
if(bet.lower()==color[j]):
    print("You win the bet")
else:
    print(f"You lost,{color[j]} turtle won the race")
screen.exitonclick()
