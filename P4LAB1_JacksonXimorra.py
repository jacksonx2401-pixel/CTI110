#Ximorra Jackson
#06/30/26
#P4LAB!
# In this assignment we are learning to make shapes using python

import turtle

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightblue")
wn.title("Tess & Alex")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.fillcolor("green")
tess.color("green")
tess.pensize(3)


alex = turtle.Turtle()    
alex.color("green")

tess.begin_fill()
tess.fillcolor("green")
tess.forward(100)             # Make tess draw equilateral triangle
tess.left(120)
tess.forward(100)
tess.left(120)
tess.forward(100)
           
for i in range(4):           # Move her away from the origin
	tess.end_fill()
alex.pensize(3)
alex.sety(-100)
for i in range(4):             # Make alex draw a square
	alex.forward(100)
	alex.left(90)



wn.mainloop()