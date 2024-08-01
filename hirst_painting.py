# import colorgram
#
# colors = colorgram.extract('hirst.jpeg', 30)
#
#
# rgb_color=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_color.append(rgb)
# print(rgb_color)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(219, 157, 85), (220, 222, 228), (226, 218, 222), (55, 109, 78), (55, 98, 150), (133, 58, 84), (114, 150, 195), (69, 160, 70), (121, 37, 51), (202, 149, 154), (225, 82, 56), (73, 38, 56), (143, 173, 152), (40, 59, 106), (217, 198, 132), (93, 122, 182), (33, 88, 52), (200, 176, 27), (142, 102, 56), (102, 42, 41), (217, 180, 174), (172, 205, 187), (219, 171, 174), (86, 32, 28), (28, 44, 83), (192, 90, 102), (185, 185, 214), (34, 66, 40)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()
