import turtle
from math import *
from random import *
from randomColors import *
# turtle.heading(rotation + n)

def setup():
    turtle.colormode(255)
    turtle.clear()
    turtle.reset()
    turtle.speed(400)
    turtle.bgcolor("black")
#   Separate function for drawing rectangle:
def turtleRectangle(h, w, rot, prot):
    turtle.setheading(rot + prot)
    turtle.pendown()
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.penup()

# Rectangle function for the turtle:
def drawRectanglePattern(x, y, wid, hei, off, rad, count, rot):
    turtle.penup()
    turtle.goto(x, y)
    # Supposed "Start point, where the rectangles are drawn with offset accounted for:
    startPt = rad + off
    ###############################################
    # Spacing along the circumference of the circle pattern:
    spacing = floor((2 * pi * rad) / (count))
    turtle.setheading(0)
    for i in range(count):
        turtle.color(redRand(), greenRand(), blueRand())
        previousRot = turtle.heading()
        previous_xy = turtle.position()
        turtleRectangle(hei, wid, rot, previousRot)
        turtle.penup()
        turtle.goto(previous_xy)
        turtle.setheading(previousRot)
        # Circle axis:
        turtle.circle(radius=startPt, extent=spacing)
# circle pattern:
def drawCirclePattern(x, y, size, off, rad, count):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    startPt = rad + off
    # spacing in degrees along axis:
    spacing = floor((2 * pi * rad) / (count))
    # loop drawing count:
    for i in range(count):
        turtle.color(redRand(), greenRand(), blueRand())
        previousRot = turtle.heading()
        previous_xy = turtle.position()
        turtle.pendown()
        turtle.circle(size)
        turtle.penup()
        turtle.goto(previous_xy)
        turtle.setheading(previousRot)
        # Circle axis:
        turtle.circle(radius=startPt, extent=spacing)
def drawSuperPattern(randNum):
    # Take turtle to designated coordinates:
    # While function handles drawing patterns:
    for i in range(randNum):
        randX = randint(-500, 500)
        randY = randint(-500, 500)
        randOff = randint(-50, 50)
        randRad = randint(1, 50)
        randW = randint(1, 50)
        randH = randint(1, 50)
        randRot = randint(0, 180)
        randCirRad = randint(0, 100)
        randChoice = randint(0, 1)
        randCount = randint(1, 100)
        if randChoice == 0:
            drawRectanglePattern(x=randX, y=randY, wid=randW, hei=randH, off=randOff, rot=randRot, count=randCount, rad=randRad)
        elif randChoice == 1:
            drawCirclePattern(x=randX, y=randY,size=randCirRad , off=randOff, count=randCount, rad=randRad)


