# draws a tree
from tkinter import N
import turtle
import random



# set the canvas window
def set_canvas():
    s = turtle.Screen()     
    s.setup(1000, 1000)
    s.bgcolor('light blue')
    s.title('Turtle Program')
    return s

# set a turtle (a pen)
def set_pen(color):         
    t = turtle.Turtle()
    t.shape('turtle')  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=10)
    return t

# draw a tree fractal using recursion
def draw_tree(t, branch, angle, n):
  if n > 0: # recursive step
        t.color('ivory')
        t.pensize(n*3)
        t.forward(branch)
        length = branch * 9/10
        t.left(angle)
        draw_tree(t, length, angle, n-1) # recursive call (left branch of the tree)
        t.right(angle*2)
        draw_tree(t, length, angle, n-1) # recursive call (right branch of the tree)
        t.pensize(n*2)
        t.color('brown')
        t.left(angle)
        t.backward(branch)    
  else: # base case
        t.color(random.randint(7, 10)/10, 0.6, 0.7)
        t.pendown()
        t.dot(15)

# main program
# s = set_canvas()
s = set_canvas()
t = set_pen('brown')
t.penup()
t.goto(0, -250)
t.left(90)
t.pendown()
draw_tree(t, 60, 25, 10)
s.exitonclick()