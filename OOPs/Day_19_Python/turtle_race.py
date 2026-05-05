from turtle import Turtle, Screen
from random import randint


tim = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
jimmy = Turtle(shape="turtle")
rommy = Turtle(shape="turtle")

turtle_screen = Screen()
turtle_screen.setup(width=500, height=400)
user_bet = turtle_screen.textinput(title="Make a bet", prompt="Which color turtle will win the race? Enter the color: ")


turt = [tim, tommy, jimmy, rommy]

def set_color():
    tim.color("red")
    tommy.color("green")
    jimmy.color("blue")
    rommy.color("indigo")

def set_position():
    y_pos = 110
    x_pos = -200
    for tur in turt:
        tur.speed("fast")
        tur.penup()
        tur.goto(x=x_pos, y=y_pos)
        y_pos -=50

set_color()
set_position()
if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in turt:
        turtles.forward(randint(0, 10))
        if(turtles.xcor() > 200):
            print("End of race")
            if user_bet == turtles.pencolor():
                print("you won")
            else:
                print(f"You loose!! The {turtles.pencolor()} turtle won the game")
            is_race_on = False
turtle_screen.exitonclick()