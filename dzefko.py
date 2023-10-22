from turtle import *
speed(2)
left(90)
'''
def dzefko(x, min_x):
    if x<min_x:
        return
    forward(x)
    left(60)
    dzefko(x/2, min_x)
    #forward(x/2)
   # right(180)
   # forward(x/2)
   # left(60)
    right(240)
    forward(x)
    left(60)
    dzefko(x/2, min_x)
    #forward(x)
    #forward(x/2)
    left(60)
    forward(x)
    left(180)
    #dzefko(x/2, min_x)
   # left(120)
    #forward(x/2)
    #forward(x)
    
    
   # forward(x)
  #  left(180)

dzefko(100, 25)
'''

def dzefko2(x,min_x):
    if x<min_x:
        return
    forward(x)
    left(60)
    dzefko2(x/2,min_x)
    left(120)
    forward(x)
    left(60)
    dzefko2(x,min_x)
    right(120)
    forward(x)
    right(180)



def dzefko3(x,n):
    if n == 0:
        return
    forward(x)
    left(60)
    #forward(x/2)
    #back(x/2)
    dzefko3(x/2,n - 1)
    right(120)
    #forward(x)
    #left(60)
    dzefko3(x/2, n - 1)
    right(120)
    forward(x)
    right(180)


dzefko3(100,4)