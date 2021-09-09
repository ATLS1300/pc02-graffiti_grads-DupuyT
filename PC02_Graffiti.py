#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Taylor Dupuy
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.setposition(-25, 185)
turtle.color("firebrick")
turtle.down()
turtle.begin_fill()
turtle.circle(35, -180)
turtle.forward(15)
turtle.circle(35, 180)
turtle.end_fill()
turtle.up()
turtle.setposition(33, 190)
turtle.down()
turtle.begin_fill()
turtle.circle(35, 180)
turtle.forward(15)
turtle.circle(35, -180)
turtle.end_fill()
turtle.up()
turtle.setposition(-300,300)
turtle.left(180)
turtle.color("OrangeRed1")
turtle.down()
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.up()
turtle.setposition(-300, 175)
turtle.left(90)
turtle.down()
turtle.forward(40)
turtle.up()
turtle.setposition(-280, 180)
turtle.setheading(290)
turtle.down()
turtle.forward(40)
turtle.up()
turtle.setposition(-260, 190)
turtle.setheading(305)
turtle.down()
turtle.forward(40)
turtle.up()
turtle.setposition(-240, 200)
turtle.setheading(320)
turtle.down()
turtle.forward(40)
turtle.up()
turtle.setposition(-220, 220)
turtle.setheading(335)
turtle.down()
turtle.forward(40)
turtle.up()
turtle.setposition(-220, 240)
turtle.setheading(355)
turtle.down()
turtle.forward(40)
turtle.up()
turtle.setposition(-360, -160)
turtle.setheading(0)
turtle.color(255, 0, 0)
turtle.pensize(10)
turtle.down()
turtle.forward(20)
turtle.circle(50, 90)
turtle.circle(-50, -90)
turtle.backward(40)
turtle.circle(-50, -90)
turtle.circle(50, -90)
turtle.backward(30)
turtle.circle(50, 90)
turtle.circle(50, 90)
turtle.circle(50, 90)
turtle.circle(-50, -90)
turtle.backward(40)
turtle.setheading(0)
turtle.circle(50,90)
turtle.circle(50,90)
turtle.backward(40)
turtle.circle(50, -90)
turtle.circle(-50, 90)
turtle.forward(40)
turtle.circle(-50, -90)
turtle.circle(-50, -70)
turtle.backward(10)
turtle.setheading(0)
turtle.forward(40)
turtle.forward(40)
turtle.circle(50, 50)
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()