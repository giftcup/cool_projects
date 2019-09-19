from turtle import *
from random import randint, choice
import time

#draw track race
speed(10)
penup()
goto(-140 , 140)

for step in range (20):
    write (step, align ='center')
    right(90)
    forward (10)
    pendown ()
    forward (250)
    penup()
    backward (260)
    left(90)
    forward (20)

goto(200, 220)
write("Finish Line", align='center')
pendown()


eposi = Turtle()
eposi.color('red')
eposi.shape('turtle')
eposi.penup()
eposi.goto(-160,100)

arrey = Turtle()
arrey.color('turquoise')
arrey.shape('turtle')
arrey.penup()
arrey.goto(-160,50)

tabi = Turtle()
tabi.color('blue')
tabi.shape('turtle')
tabi.penup()
tabi.goto(-160,0)

lyonga = Turtle()
lyonga.color('yellow')
lyonga.shape('turtle')
lyonga.penup()
lyonga.goto(-160,-50)

keming = Turtle()
keming.color('orange')
keming.shape('turtle')
keming.penup()
keming.goto(-160,-100)

turtle = choice([tabi,keming,lyonga,arrey,eposi])
while True:
    turtle = choice([tabi,keming,lyonga,arrey,eposi])
    eposi.forward(randint(1,5))
    arrey.forward(randint(1,5))
    tabi.forward(randint(1,5))
    lyonga.forward(randint(1,5))
    keming.forward(randint(1,5))

#define winner
    if turtle.xcor()>220:
        turtle.color('purple')
        time.sleep(5)
        break
print(turtle + "won.")
