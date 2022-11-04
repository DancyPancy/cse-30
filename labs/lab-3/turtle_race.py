# turtle race
from turtle import *
from random import randint

def set_turtles(colors):
    turtles = []
    for color in colors:
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.speed(1)
        turtles.append(t)
    return turtles

def draw_track(start, finish):
    t = Turtle()
    t.speed(0)
    position, size, step = 100, 200, 40
    count = 0
    for line in range(start, finish + step, step):
        t.penup()
        t.goto(line,position+10)
        if line == start:
            t.color("blue")
            t.pensize(10)
            t.write("START")
        elif line == finish:
            t.color("red")
            t.pensize(10)
            t.write("FINISH")
        else:
            t.color("grey")
            t.pensize(1)
            t.write(count)
        t.goto(line,position)
        count += 1
        t.right(90)
        t.pendown()
        t.forward(size)
        t.left(90)
    
def isfinish(t, finish):
    x, y = t.pos()
    if x < finish:
        return False
    else:
        return True

def race(turtles, start, finish):
    # y position
    position = 80
    distance = 40
    for t in turtles:
        t.penup()
        t.left(180)
        t.goto(start, position)
        position -= distance
        t.left(180)
        t.pendown()
    done = False
    while not done:
        for t in turtles:
            t.forward(randint(1,10))
            if isfinish(t, finish):
                done = True         

def run_game(start, finish):
    s.clear()
    draw_track(start, finish)
    turtles = set_turtles(["yellow", "crimson", "aqua", "green", "purple"])
    race(turtles, start, finish)

# main program
s = Screen()     # make a canvas window
s.setup(500, 400)
s.bgcolor("white")
s.title("Turtle Race")
start = -200  # x position
finish = 200  # x position

run_game(start, finish)