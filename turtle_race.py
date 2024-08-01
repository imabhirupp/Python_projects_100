import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which color turtle will win the race? "
                                             "Choose your color(red/green/blue/orange/black) ?")

print(user_bet)

color = ["red", "green", "blue", "orange", "black"]
y = [-70, -40, -10, 20, 50]
all_turtles = []

is_game_on = False

for turtle_index in range(0,5):
    new_turtle = Turtle("turtle")   # giving the turtle a shape of an actual turtle
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])  # sending the turtle to the left side i.e. the beginning of the screen
    all_turtles.append(new_turtle)  # storing the values of new_turtle in all_turtle

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:    # all the stored turtles in the all_turtle list is called
        if turtle.xcor() > 230:   # the co-ordinates are checked of each turtle with the finish line i.e. screen end
            is_game_on = False
            winning_color = turtle.pencolor()   # to get the pen color of the turtle and not the filling color
            if winning_color == user_bet:
                print(f"You have Won! And the winning color is {winning_color}")
            else:
                print(f"You have Lost! And the winning color is {winning_color}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
