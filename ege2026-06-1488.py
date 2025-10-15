from turtle import *
size = 15
x, y = xcor(), ycor()
for i in range(2):
    begin_fill()
    x, y = x + 3, y + 4
    setpos(x*size, y*size)
    x, y = x - 3, y + 4
    setpos(x*size, y*size)
    x, y = x - 3, y - 4
    setpos(x*size, y*size)
    x, y = x + 3, y - 4
    setpos(x*size, y*size)
    end_fill()

canvas = getcanvas()
count = 0

for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x*size, y*size, x*size, y*size) == (5,6):
            count +=1
print(count)
done()