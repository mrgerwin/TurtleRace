from turtle import *

#Key Event Handlers

def keyleft():
    left(5)
    print('left')
def keyright():
    right(5)
    print('right')
def keyup():
    print('up')
    forward(10)
def keydown():
    print('down')
    backward(10)

screen = Screen()
screen.bgpic('race4.png')
screen.setup(width=1000, height=563)

#Putting turtle at Start Line
penup()
goto(50,200)
pendown()

listen()

onkey(keyup, 'Up')
onkey(keydown, 'Down')
onkey(keyleft, 'Left')
onkey(keyright, 'Right')

mainloop()
