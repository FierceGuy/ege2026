from turtle import *
k = 3
pd()
for _ in range(3):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)
pu()
forward(1*k)
right(90)
forward(5*k)
left(90)
pd()
for _ in range(3):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
done()
canvas = getcanvas()
for x in range(-100, 100):
    for y in range(-100, 100):
        canvas.find_overlapping(x*k, y*k, x*k, y*k)
