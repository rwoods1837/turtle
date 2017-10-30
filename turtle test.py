import random
from turtle import *

angle = 5
length = 5
michaelangelo = Turtle()
leonardo = Turtle()
raphael = Turtle()
donatello = Turtle()
screensize(1200,620)
colormode(255)

michaelangelo.shape("turtle")
michaelangelo.color("DarkOrange1")

leonardo.shape("turtle")
leonardo.color("blue")

raphael.shape("turtle")
raphael.color("red")
raphael.penup()
raphael.forward(100)
raphael.pendown()

donatello.shape("turtle")
donatello.color("purple")
donatello.penup()
donatello.left(180)
donatello.forward(100)
donatello.pendown()

def draw_star():
    forward()
    left(170)

def large_circle():
    leonardo.left(5)
    leonardo.forward(5) 

def small_circle():
    leonardo.left(15)
    leonardo.forward(5)

def spiral(angle,length):
    michaelangelo.forward(length)
    michaelangelo.right(angle)
    
for i in range(24):    
    small_circle()

for i in range(72):
    large_circle()

for i in range(72):
    raphael.forward(10)
    raphael.left(10)

    donatello.forward(10)
    donatello.right(10)

while True:
    for i in range(72):
        leonardo.left(5)
        raphael.left(25)
        donatello.left(45)

        spiral(angle,length)
        False

clear()
reset()

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
        
