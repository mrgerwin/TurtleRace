from turtle import *

#Key Event Handlers

def keyleft():
    player1.left(5)
   
def keyright():
    player1.right(5)
    
def keyup():
    player1.forward(10)
    
def keydown():
    player1.backward(10)
    
def keya():
    player2.left(5)

def keyw():
    player2.forward(10)

def keys():
    player2.backward(10)

def keyd():
    player2.right(5)

screen = Screen()
screen.bgpic('race4.png')
screen.setup(width=1000, height=563)

player1 = Turtle()
player2 = Turtle()
player2.pencolor('red')
player2.fillcolor('red')

#Putting player1 at Start Line
player1.penup()
player1.goto(50,200)
player1.pendown()

#Putting player2 at Start Line
player2.penup()
player2.goto(50,220)
player2.pendown()

listen()

onkey(keyup, 'Up')
onkey(keydown, 'Down')
onkey(keyleft, 'Left')
onkey(keyright, 'Right')
onkey(keya, 'a')
onkey(keys, 's')
onkey(keyd, 'd')
onkey(keyw, 'w')


mainloop()
