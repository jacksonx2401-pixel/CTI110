#Ximorra Jackson
#06/30/26
#P4LAB!
# In this assignment we are learning to make shapes using python

import turtle

# --- Set up the window ---
wn = turtle.Screen()         
wn.bgcolor("lightblue")
wn.title("Tess & Alex Build a House")

# --- Create Tess (The Roof Builder) ---
tess = turtle.Turtle()       
tess.color("green")
tess.fillcolor("green")
tess.pensize(3)
tess.speed(3)

# --- Create Alex (The Base Builder) ---
alex = turtle.Turtle()    
alex.color("green")
alex.fillcolor("lightblue")
alex.pensize(3)
alex.speed(3)

# --- 1. Alex draws the house base using a FOR loop ---
alex.begin_fill()
for _ in range(4):             # Loops exactly 4 times for a square
    alex.forward(100)
    alex.left(90)
alex.end_fill()

# --- 2. Move Tess to the top of the square using a WHILE loop ---
# We use a while loop here to move Tess up step-by-step to the roof line
tess.penup()
while tess.ycor() < 100:       # Keep moving up until Y coordinate is 100
    tess.sety(tess.ycor() + 10) 
tess.pendown()

# --- 3. Tess draws the roof triangle using a FOR loop ---
tess.begin_fill()
for _ in range(3):             # Loops exactly 3 times for a triangle
    tess.forward(100)
    tess.left(120)
tess.end_fill()

# Keep window open
wn.exitonclick()
