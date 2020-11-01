#Justine Rosado
#10/28/20
#this code is supports to let you comman the polygon of what you want the size to be and fill in the color inside of the polygon.


import turtle

def polygon(side,length,color):
    t=turtle.Turtle()
    t.fillcolor('blue')
    t.begin_fill()
    for num in range(side):
        t.right(360/side)
        t.forward(length)
    t.end_fill()
    for color in color:
        print(color)
sides=int(input("how many sides?"))
sidelength=int(input("what is the sidelength?"))
color=str(input("what is the color?"))
polygon(sides,sidelength,color)


        
        



