import turtle

def set_pen():
    t = turtle.Turtle()
    t.color('red')
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


def polygon(size, n):
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.forward(size)
        t.left(360/n)
    t.end_fill()
    t.penup()

def polygon_wrapper(size, n):
    alpha = 360/n
    t.pendown()
    t.begin_fill()
    polygon_recursive(size, n, alpha)
    t.end_fill()
    t.penup()

def polygon_recursive(size, n, alpha):
    if n > 0:
        t.forward(size)
        t.left(alpha)
        polygon_recursive(size, n-1, alpha)

def star(size, n, d=2):
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.forward(size)
        t.left(d * 360 / n)
    t.end_fill()
    t.penup()

def star_wrapper(size, n, d=2):
    alpha = 360/n
    t.pendown()
    t.begin_fill()
    star_recursive(size, n, alpha, d)
    t.end_fill()
    t.penup()

def star_recursive(size, n, alpha, d=2):
    if n > 0:
        t.forward(size)
        t.left(d * alpha)
        star_recursive(size, n-1, alpha, d)

if __name__ == '__main__':
    #initialize the pen and the screen window
    s = set_canvas()
    t = set_pen()

    #draw shapes
    t.goto(300, -200)
    star(100, 13 , 3)

    t.goto(270, 250)
    t.color('green')
    star_wrapper(150, 9, 2)

    t.goto(-300, 300)
    t.color('orange')
    polygon(200, 3)

    t.goto(-300, -300)
    t.color('purple')
    polygon_wrapper(300, 6)

    #close program on click of window
    s.exitonclick()