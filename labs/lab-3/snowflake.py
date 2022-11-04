from math import sqrt
import turtle

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


def draw_snowflake(size, n):
    if n > 1:
        draw_snowflake(size/3, n - 1)
        t.left(60)
        draw_snowflake(size/3, n - 1)
        t.right(120)
        draw_snowflake(size/3, n - 1)
        t.left(60)
        draw_snowflake(size/3, n - 1)
    else:
        t.forward(size)

if __name__ == '__main__':
    s = set_canvas()
    t = set_pen()
    
    size = 500
    
    t.goto(-size/2, -size/(2*sqrt(3)))
    t.pendown()
    t.left(60)

    for i in range(3):
        draw_snowflake(size, 10)
        t.right(120)

    s.exitonclick()
