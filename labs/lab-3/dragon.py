import turtle
import math

def set_pen():
    t = turtle.Turtle()
    t.color('black')
    t.speed(10)
    t.shape('turtle')
    t.pensize(2)
    t.penup()
    return t

def set_canvas():
    s = turtle.Screen()     
    s.setup(1000, 1000)
    s.bgcolor('light grey')
    s.title('Turtle Program')
    return s

def draw_dragon(size, n):
    if n == 0:
        t.forward(abs(size))
    else:
        t.right(size/abs(size)*45)
        draw_dragon(abs(size)/math.sqrt(2), n-1)
        t.left(size/abs(size)*90)
        draw_dragon(-abs(size)/math.sqrt(2), n-1)
        t.right(size/abs(size)*45)

if __name__ == '__main__':
    s = set_canvas()
    t = set_pen()

    size = 500

    t.goto(-size/2, 0)
    t.pendown()
    draw_dragon(size, 5)
    t.penup()

    s.exitonclick()