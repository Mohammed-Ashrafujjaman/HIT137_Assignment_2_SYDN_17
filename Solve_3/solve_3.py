'''
Create a program that uses a recursive function to generate a geometric pattern using 
Python's turtle graphics. The pattern starts with a regular polygon and recursively 
modifies each edge to create intricate designs. 

Pattern Generation Rules: 
For each edge of the shape: 
    1. Divide the edge into three equal segments 
    2. Replace the middle segment with two sides of an equilateral triangle pointing 
    inward (creating an indentation) 
    3. This transforms one straight edge into four smaller edges, each 1/3 the length of 
    the original edge 
    4. Apply this same process recursively to each of the four new edges based on the 
    specified depth 
    
Visual Example: 
    Depth 0: Draw a straight line (no modification) 
    Depth 1: Line becomes: ——\⁄—— (indentation pointing inward) 
    Depth 2: Each of the 4 segments from depth 1 gets its own indentation 

User Input Parameters: 
The program should prompt the user for: 
    Number of sides: Determines the starting shape 
    Side length: The length of each edge of the initial polygon in pixels 
    Recursion depth: How many times to apply the pattern rules 

Example Execution: 
Enter the number of sides: 4 
Enter the side length: 300 
Enter the recursion depth: 3

'''

'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

import turtle
from termcolor import colored


def input_validation(x, name):
    # Assigned to pujan
    pass 

def draw_edge(t, length, depth):
    # assigned to Al-amin Dhaly
    pass

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
