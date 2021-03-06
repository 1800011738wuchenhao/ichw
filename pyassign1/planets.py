import math
import turtle
wn=turtle.Screen()
turtle.bgcolor('black')
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
e=turtle.Turtle()
f=turtle.Turtle()

sun=turtle.Turtle()
sun.shape("circle")
sun.color('orange')
sun.turtlesize(2)

def planet(name,color):
    name.pencolor(color)
    name.color(color)
    name.shape("circle")
    name.speed(0)
planet(a,'blue')
planet(b,'green')
planet(c,'red')
planet(d,'pink')
planet(e,'yellow')
planet(f,'brown')

def origin(t,x):
    t.up()
    t.goto(x,0)
    t.down()
origin(a,35)
origin(b,56)
origin(c,77)
origin(d,98)
origin(e,119)
origin(f,140)
    
def orbit(t,a,e,o):    
    r=a*(1-e**2)/(1+e*math.cos(math.radians(o)))
    x=r*math.cos(math.radians(o))
    y=r*math.sin(math.radians(o))
    t.goto(x,y)

for o in range(1440):
    orbit(a,50,0.3,8*o)
    orbit(b,80,0.3,8*o/2.023857703)
    orbit(c,110,0.3,8*o/3.263127334)
    orbit(d,140,0.3,8*o/4.685296149)
    orbit(e,170,0.3,8*o/6.269290231)
    orbit(f,200,0.3,o)