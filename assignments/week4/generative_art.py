# import turtle
from turtle import*
import random


# parameters
width = 500
height = 800
size = 50
noise = 1

# general setup
setup(width, height)
tracer(0, 0) # disable animation
bgcolor("black")

# red triangles (not filled)
color("red")
for y in range(20):
    for x in range(15):
        # move starting point
        penup()
        goto(-width/2 + x*size, height/2 - y*size)
        pendown()
        #rotate
        angle = random.uniform(-noise, noise)
        right(angle)
        # draw square
        for i in range(6):
            forward(size) # draw from starting point, go forward
            right(120) # turn 120 degrees
        left(angle)
    noise += 8

# yellow circles (filled)
fillcolor("yellow")
num_circles = 15
for _ in range(num_circles):
    # position
    x = random.randint(-width // 2, width // 2)
    y = random.randint(-height // 2, height // 2)

   # radius
    radius = random.randint(10, 50)

    penup()
    goto(x, y)
    pendown()

    begin_fill()
    circle(radius)
    end_fill()


penup()
done() # important to keep at the end
