import turtle
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def forward():
    turtle.forward(10)
def backward():
    turtle.back(10)

def left():
    turtle.left(10)

def right():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")



screen.exitonclick()
