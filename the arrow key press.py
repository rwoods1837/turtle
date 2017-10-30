from turtle import *
setup(500, 500)
Screen()
title("Turtle Keys")
ryan = Turtle()
showturtle()
ryan.speed(10)
ryan.width(10)

def forward():
    ryan.forward(10)

def left_key():
    ryan.left(15)

def right_key():
    ryan.right(15)

def go_back():
    ryan.back(10)
 
def space_bar():
    if ryan.isdown():
        ryan.penup()

    else:
        ryan.pendown()

def red():
    ryan.color(1,0,0)

def green():
    ryan.color(0,1,0)

def blue():
    ryan.color(0,0,1)

def back():
    ryan.undo()

def clear():
    ryan.clear()

onkeypress(forward, "Up")
onkeypress(left_key, "Left")
onkeypress(right_key, "Right")
onkeypress(go_back, "Down")
onkeypress(space_bar, "space")
onkeypress(red, "r")
onkeypress(green, "g")
onkeypress(blue, "b")
onkeypress(back, "BackSpace")
onkeypress(clear, "c")

listen()
mainloop()
