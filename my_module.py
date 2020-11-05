import random

import math

def k():
    for n in range(10):
        print(random.randint(25,35))

def o(items):
    return(random.choice(items))
    
    
    

def n():
    for n in range(20):
        odd= random.randint(0,100)
        if odd%2 == 1:
            return(odd)
            break
        

n()

def c(a,b):
    c=0
    c=(math.sqrt((a*a)+(b*b)))
    return(c)
