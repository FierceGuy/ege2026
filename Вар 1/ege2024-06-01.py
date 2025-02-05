from turtle import *
tracer(0)

left(90)
k = 10
pd()
# Повтори 2 
for _ in range(2):
    forward(16 * k)#[Вперёд 16 ]
    right(90) #Направо 90 
    forward(9 * k) # Вперёд 9 
    right(90) #Направо 90

# Поднять хвост
pu()
forward(5 * k) # Вперёд 5
right(90) #Направо 90
forward(11 * k) #Вперёд 11
right(90) #Направо 90

# Опустить хвост
pd()
for _ in range(2): # Повтори 2 
    forward(20 * k)#[Вперёд 20
    right(90) #Направо 90
    forward(8 * k) #Вперёд 8
    right(90) #Направо 90]

pu()
# делаем разметку
for x in range(-20, 20):
    for y in range(-20, 20):
        goto (x * k, y * k)
        dot(5)
done()