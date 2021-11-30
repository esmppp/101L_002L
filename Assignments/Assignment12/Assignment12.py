# Ethan Miller, esmppp@umsystem.edu, CS101L 11/29/2021
import turtle
from Point import *
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        '''Draws a Box'''
        turtle.setheading(0)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class FilledCircle(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

turtle.forward(100)
turtle.right(90)
turtle.forward(50)

p= Point(-100,100,'blue')
p.draw()

c = Box(-100, 100, 50, 20, "blue")
c.draw()

b = BoxFilled(1,2,100,200,'red','blue')
b.draw()

d = Circle(300, 50, 50, 'yellow')
d.draw()

e = FilledCircle(-100, -50, 70, 'purple', 'orange')
e.draw()
e.fillcolor = 'green'