def info():
    """Any variable created within any condition or loop, it can be accessed outside the block unless 
    those conditions or loops are in a function. Then those variables can't ba accessed outside the function"""
    print("Read the info about this file")
    print("Uncomment the last print in line 35 and try to see")
#
info()
name1 = "Hi" #Global scope
#Local scope
def name():
    name1 = "Vivek"
    print(name1) # Local scope O/P : Vivek

name()
print(name1) # Get data from global scope O/P: Hi


# There is not block scope concept in python
track = 0
if track  == 0:
    feedback = 0
else:
    feedback = 1

print(feedback) # Feedback is still accessable even out of the if block

def test_scope():
    track = 0
    if track  == 0:
        feedback_test = 0
    else:
        feedback_test = 1
    print(feedback_test)

#print(feedback_test) #Here not accessable as feedback is defined in function


enemies = 1
def increase_enemies(enemies):
    """Gives better understanding on modifying globla 
    variables and use of global keyword and it's complications"""
    enemy = enemies
    print("#global enemies")  
    print("This would give access global variables, although it's not recommended. This would confuse and might lead to manual programming errors")
    # enemies += 1
    enemy += 1
    print(enemies)
    print("return enemies ")
    print("This is a better choice")
    return enemy

enemies = increase_enemies(enemies)


# global constants and constants in general are written in capital letter to indicate them as global variables for user
PI = 3.142
print(enemies)
PI += 1  #But it doesn't restrict from changing the value unlike in C and C++
print(PI)

def change_value():
    global PI
    PI += 1
    print("Was able to access and update using global keyword")

change_value()
print(f"It still didn't restrict value change for PI = {PI} in function")