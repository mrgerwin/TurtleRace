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
    #delete pass and use this section to program a rightU
    pass

screen = Screen()
screen.bgpic('Race2.png')
screen.setup(width=275, height=200)

penup()
goto(-5,-65)
pendown()

#### start using the functions below this line.

