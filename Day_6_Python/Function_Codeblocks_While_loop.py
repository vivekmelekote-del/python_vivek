#Code blocks, Functions, While loops
#In built functions : https://docs.python.org/3/library/functions.html
#User defined functions

#def is a keywork. defining a function. Followed by function_name.
# def my_functio():
#     print("Hello")
#     print("Bye")
    
#my_functio() #Calling the function

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json Tryout

output = 0
def add_number():
    global output
    output = (a + b)
def sub_number():
    global output
    output = (a - b)
def mul_number():
    global output
    output = (a * b)
def div_number():
    global output
    output = (a / b)

a = 0
b = 0
operation = ""

a = int(input("First number\n"))
while(True):
    operation = input("Operation\n")
    if(operation == "="):
        print(output)
        exit(0)
    b = int(input("Second number\n"))
    if(operation == "+"):
        add_number()
    if(operation == "-"):
        sub_number()
    if(operation == "*"):
        mul_number()
    if(operation == "/"):
        div_number()


#Solution to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json
# def right():
#     turn_left()
#     turn_left()
#     turn_left()
#     #f(front_is_clear()):
#     move()
# def check_left():
#     turn_left()
#     if(front_is_clear()):
#         move()
#     else:
#         right_1()
#         #move()
#         #move()
# while(front_is_clear()):
#     move()
# turn_left()
# def right_1():
#     right()
#     #move()
#     if(not front_is_clear()):
#         right()
#     #move()
# while(not at_goal()):
#     if(right_is_clear()):
#         right()
#     elif(wall_on_right() and front_is_clear()):
#         move()
#     else:
#         turn_left()
        
