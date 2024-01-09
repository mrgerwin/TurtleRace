from turtle import *

def straightaway():
    forward(100)
    
def leftcorner():
    left(45)
    forward(20)
    left(45)

def leftU():
    leftcorner()
    forward(10)
    leftcorner()

def rightU():
    right(45)
    forward(20)
    right(45)
    forward(10)
    right(45)
    forward(20)
    right(45)

screen = Screen()
screen.bgpic('Race2.png')
screen.setup(width=275, height=200)

penup()
goto(-5,-65)
pendown()

#### DO NOT MODIFY ANYTHING ABOVE HERE

straightaway()
leftcorner()
straightaway()
leftcorner()
straightaway()
forward(75)
leftcorner()
forward(20)
leftcorner()
forward(75)
rightU()
forward(75)
leftU()
forward(75)