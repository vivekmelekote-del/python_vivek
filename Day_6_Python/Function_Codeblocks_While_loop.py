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
def add_number(a, output):
    """Performs addition of
     2 numbers"""
    print(a, output)
    return (output + a)
def sub_number(a, output):
    """Performs substraction
     of two numbers"""
    print(a, output)
    return (output - a)
def mul_number(a, output):
    """Performs multiplication 
    of two numbers"""
    print(a, output)
    return (output * a)
def div_number(a, output):
    """Performs division of
    two numbers"""
    print(a, output)
    return (output / a)

a = 0
b = 0
operation = ""

def old_calculator():
    """Added this function after learning about and function with output"""
    output = float(input("First number\n"))
    while(True):
        print(f" '+' : Addition\n'-' : substraction\n'*' : Multiplication\n'/' : division\n'=' : get output and exit")
        operation = input("Operation\n")
        if(operation == "="):
            print(output)
            exit(0)
        a = float(input("Second number\n"))
        if(operation == "+"):
            output = add_number(a, output)
        if(operation == "-"):
            output = sub_number(a, output)
        if(operation == "*"):
            output = mul_number(a, output)
        if(operation == "/"):
            output = div_number(a, output)

def new_calculator():
    """Added this function after learning about dictionaries 
    and function with output"""
    Calculator_dictionary = {}
    output = float(input("First number\n"))
    while(True):
        Addition = add_number
        substraction = sub_number
        Multiplication = mul_number
        division = div_number
        Calculator_dictionary['+'] = Addition
        Calculator_dictionary['-'] = substraction
        Calculator_dictionary['*'] = Multiplication
        Calculator_dictionary['/'] = division
        Calculator_dictionary['='] = "exit_with_output"
        print(f" '+' : Addition\n'-' : substraction\n'*' : Multiplication\n'/' : division\n'=' : get output and exit")
        operation = input("Operation\n")
        if(operation == "="):
            print(output)
            exit(0)
        else:
            a = float(input("Second number\n"))
        if(operation == "+"):
            output = Calculator_dictionary[operation](a, output)
        if(operation == "-"):
            output = Calculator_dictionary[operation](a, output)
        if(operation == "*"):
            output = Calculator_dictionary[operation](a, output)
        if(operation == "/"):
            output = Calculator_dictionary[operation](a, output)


choose_calculator = input("Choose from old or new calculator: ")
if(choose_calculator == 'old'): #Uses direct functionall
    old_calculator()
elif(choose_calculator == 'new'): #Uses someting like function pointer.
    #The function is stored in dictionary, and based on operatio, we choose the key to call the function
    new_calculator()
else:
    print("Wrong choice")
    print("Exiting the calculator program")

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
        
