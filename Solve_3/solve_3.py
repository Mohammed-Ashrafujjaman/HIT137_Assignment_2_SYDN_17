
'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

import turtle
from termcolor import colored # this is for colored output in terminal


def input_validation(x, name):
    # Assigned to pujan
    pass 

def draw_edge(t, length, depth):
    # Base case: if depth is 0, just draw a straight line
    # Al-Amin Dhaly's Part
    if depth == 0:
        t.forward(length)
    else:
        # Divide length into 3 smaller parts
        segment = length / 3

        # Recursive step
        draw_edge(t, segment, depth - 1)  # First third
        t.left(60)                        # Turn left to draw indentation
        draw_edge(t, segment, depth - 1)  # First side of the triangle
        t.right(120)                      # Turn right
        draw_edge(t, segment, depth - 1)  # Second side of the triangle
        t.left(60)                        # Turn back
        draw_edge(t, segment, depth - 1)  # Last third


def draw_pattern(sides, length, depth):
    # assigned to Ashraf
    # This angle is to create a rotation 
    angle = 360 / sides

    # starting turtle, A GUI library to draw something
    t = turtle.Turtle()
    # Determining the speed
    t.speed(0)
    # hiding turtle head increase the drawing speed. 
    t.hideturtle()

    # this line is for adjusting the starting point to start drawing in the GUI
    t.penup()
    # Adjusting the starting point from which coordinate the the drawing going to start
    t.goto(-200, -150)  
     # this line will draw the first edge horizontal (drawing will start from the given point to right hand side)
    t.setheading(0) 
    # setting the pointer to start drawing
    t.pendown()

    # start drawing according to side.
    for _ in range(sides):
        # calling the draw_edge with the parameter t=turtle, length = length of the side, depth = recursion depth
        draw_edge(t, length, depth)
        # turning the sides counter-clockwise for rotation 
        t.left(angle)  

    turtle.done()


def main():
    # Main funciton -> Imtiaz
    pass

    
if __name__ == "__main__":
    main()
   

'''
References :
youtube: https://youtu.be/DaTsozguU4U
stack Overflow: https://stackoverflow.com/questions/39687393/stepping-through-python-turtle-recursive-function?utm_source=chatgpt.com
'''