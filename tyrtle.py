from turtle import *
import time
left(90)

"""
def trojkaty(x, min_x):
    if (x<min_x):
            return
    
    for i in range (3):
        
        right(30)
        forward((4/3)*x)
        right(120)
        forward(x/3)
        right(120)
        forward(x/3)
        left(150)
    trojkaty(x/2, 60)

trojkaty(100, 30)
time.sleep(100)
"""
right(30)
def trojkaty1 (x, min_x):
    if (x<min_x):
        return
    for i in range (3):
        forward(x)
        trojkaty1(x/2,min_x)
        right(120)
    
trojkaty1(100, 10)