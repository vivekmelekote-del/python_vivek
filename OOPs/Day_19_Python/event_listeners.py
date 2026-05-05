from turtle import Turtle, Screen
from random import randint


tim = Turtle()

turtle_screen = Screen()

def move_forward():
    tim.forward(50)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def turn_back():
    tim.back(50)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def circle_on_key():
    tim.speed("slow")
    tim.circle(50)

turtle_screen.listen()
turtle_screen.onkey(move_forward, 'w')
turtle_screen.onkey(turn_right, 'a')
turtle_screen.onkey(turn_left, 'd')
turtle_screen.onkey(turn_back, 's')
turtle_screen.onkey(clear_screen, 'c')
turtle_screen.onkey(circle_on_key, 'q')
turtle_screen.exitonclick()