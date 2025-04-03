from turtle import *
from math import *

speed(10)  

R = 250

pu()
for w in range(0, 360, 1):  # Шаг 1 градус
    x = R * cos(radians(w))  # Переводим градусы в радианы
    y = R * sin(radians(w))
    goto(x, y)
    pd()

done()
