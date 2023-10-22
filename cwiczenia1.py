from turtle import *
speed(0.1)
left(90)
def spirala(x,min_x):
    if x<min_x:
        return
    forward(x)
    right(90)
    spirala(x-5,min_x)
    right(90)
    forward(x)
    right(180)

def luczek(x,min_x):
    if x<min_x:
        return
    forward(x)
    right(45)
    luczek(x-5,min_x)

    right(135)
    forward(x)
    right(180)

def luczek1(x,min_x):
    if x<min_x:
        return
    forward(x)
    right(60)
    luczek1(x/2,min_x)
    left(120)
    luczek1(x/2,min_x)
    
    left(120)
    forward(x)
    right(180)



def inny_luczek(x,max_x):
    if x>max_x:
        return
    forward(x)
    left(45)
    inny_luczek(x+5,max_x)

#def galaz(x,min_x):


#spirala(100,10)
luczek1(100,5)
#inny_luczek(10,100)