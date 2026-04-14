#Tuples
my_tuples = (1, 2, 3, 4, 7, 8, 5) #This is a tuple defnition
print(my_tuples[0]) # Way to access data in a tuple.
# my_tuples[0] = 100 This operation is not possible, as data in a tuple is not modifyable, can't remove from tuple
# Tupleas are IMMUTABLE
# Color mix and matching: https://www.w3schools.com/colors/colors_rgb.asp

import turtle as t
# import colorgram If we need to use this, we have to build file using command .\.venv\Scripts\python.exe OOPs\Day_18_Python\tuples_user.py

from random import randint, choice
timmy = t.Turtle()
t.colormode(255) # This is tapping into turtle librery and changing the 

def color_choose():
    r = randint(0, 200)
    g = randint(0, 200)
    b = randint(0, 200)
    random_color = (r,g,b)
    return random_color

def create_screen_and_turtle():
    """Give shape to turtle"""
    timmy.shape("turtle")
    
def exitscreen():
    """Creates a screen and exits on click"""
    screen = t.Screen()
    screen.exitonclick()

def random_movement():
    i = 0
    turtle_movement = [0, 90, 180, 270]
    timmy.pensize(10)
    for _ in range(1, 11):
        timmy.speed("fastest") #"slowest", "slow","normal", "fase", "fastest"
        timmy.color(color_choose())
        timmy.right(choice(turtle_movement))
        timmy.forward(50)
        timmy.left(choice(turtle_movement))

# create_screen_and_turtle()
# random_movement()
# exitscreen()

#---------------to draw a corcle with different colors and the circle shifts by some degree--------------#
def circles(i):
    timmy.circle(100)
    # timmy.right(10) #This is valid too, but the below on e does the same
    timmy.setheading(10 + timmy.heading()) #The above on is much better to use. Here 1 is the gap size between 2 circles
    # timmy.heading() gets the current headding (Angle).  setheading() sets the new direction or angle of turtle

# create_screen_and_turtle()
# # t.circle(50)
# for i in range(360 // 10):#This line with timmy.setheading(10 + timmy.heading()) this gives total number of circles
#     timmy.color(color_choose())
#     timmy.speed("fastest")
#     circles(i)
# # t.circle(50)
# # t.circle(50)
# # random_movement()
# exitscreen()

#------------------Spyrograph---------------#
from pathlib import Path

list_colors = []
# image_path = Path(__file__).parent / "image.jpg"
# colors = colorgram.extract(str(image_path), 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list_colors.append((r, g, b))

# Hirst painint
def move_with_color(list_colors):
    """Fill a 10 circle repeatedly spaced by 50"""
    for _ in range(1, 11):
        #t.colormode(255) # This is tapping into turtle librery and changing the 
        timmy.color(choice(list_colors))
        timmy.speed("fastest")
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.forward(50)

def move_turtle(x, y):
    """To set the turtle position"""
    timmy.penup()
    timmy.setx(x)
    timmy.sety(y)
    return y + 50

list_colors = [(189, 207, 249), (254, 203, 234), (193, 244, 207), (188, 174, 161), (102, 115, 126), (249, 172, 165), (210, 192, 154), (161, 193, 246), (152, 158, 165)]
create_screen_and_turtle()
y = -180
for _ in range(1, 11):
    y = move_turtle(-180, y)
    move_with_color(list_colors)
exitscreen()