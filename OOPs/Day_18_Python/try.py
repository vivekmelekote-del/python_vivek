from turtle import Turtle, Screen
from random import choice
# shape = [[3, "red", (180 - 60)], 
#                  [4, "coral", (180 - 90)],
#                  [5, "green", (180 - 108)],
#                  [6, "blue", (180 - 120)], 
#                  [7, "indigo", (180 - 128.57)],
#                  [8, "white smoke", (180 - 135)],
#                  [9, "purple", (180 - 140)], 
#                  [10, "grey", (180 - 144)]
#         ]

# print(shape[7][2])
# for i in shape:
#     print(f" i = {i}")
#     for j in i:
#         print(j)
turtle_1 = Turtle()
colout_list = ["coral", "green", "blue", "indigo", "white smoke", "purple", "grey"]

def straight_call(shape):
    """To move the turtle straight"""
    turtle_1.forward(shape)

# def move_turtel(shape):
#     angle = 360 / shape
#     for i in range(shape):
#         straight_call(100)
#         turtle_1.right(angle)

# for i in range(3, 11):
#     turtle_1.shape("turtle")
#     turtle_1.color(choice(colout_list))
#     move_turtel(i)

# screen = Screen()
# screen.exitonclick()

def straight_call(shape):
    """To move the turtle straight"""
    turtle_1.forward(shape)

def move_turtel_right(shape):
    angle = 360 / shape
    for i in range(shape):
        straight_call(100)
        turtle_1.right(angle)


def move_turtel_left(shape):
    angle = 360 / shape
    for i in range(shape):
        straight_call(100)
        turtle_1.left(angle)

#Move the turtle in random direction
def random_movement(): #Simplst way to do this is in tuples_user.py
    i = 0
    turtle_movement = [0, 90, 180, 270]
    turtle_1.pensize(10)
    # turtle_movement = [turtle_1.left(90),
    #                 turtle_1.back(50),
    #                 turtle_1.forward(50),
    #                 turtle_1.back(50),
    #                 turtle_1.left(90),
    #                 turtle_1.back(50),
    #                 turtle_1.right(90),
    #                 turtle_1.left(90),
    #                 turtle_1.forward(50),
    #                 turtle_1.forward(50),
    #                 turtle_1.left(90),
    #                 turtle_1.back(50),
    #                 turtle_1.forward(50),
    #                 turtle_1.left(90),
    #                 turtle_1.back(50)]
    for _ in range(1, 11):
        turtle_1.speed("fastest") #"slowest", "slow","normal", "fase", "fastest"
        turtle_1.pencolor(choice(colout_list))
        turtle_1.right(choice(turtle_movement))
        turtle_1.forward(50)
        turtle_1.left(choice(turtle_movement))

i = 0
turtle_1.shape("turtle")
turtle_1.color("red")
while i < 5:
    random_movement()
    i += 1
screen = Screen()
screen.exitonclick()