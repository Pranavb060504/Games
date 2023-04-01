from turtle import Screen,Turtle
import time
from snakeclass import Snake
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)
snake=Snake(10)
game_on=True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game_on==True:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if(snake.alive==False):
        break
print(f"GAME OVER,YOUR SCORE WAS:{snake.f.count}")
screen.exitonclick()

