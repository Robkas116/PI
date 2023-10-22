from turtle import *
left(60)

def gwiazdka(x, min_x):
    float(x)
    if x<min_x:
        return
    for i in range(3):
        forward(x/4)
        left(60)
        gwiazdka((x/2), min_x)
        right(60)
        forward((3/4)*x)
        right(120)
    

gwiazdka(120, 30)
