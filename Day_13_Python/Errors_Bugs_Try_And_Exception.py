from random import randint
age = int(input("Enter your age")) #If the user enters age in letters, this line will giveout an error

if age > 18:
    print(f"Your age is {age}")

# To avoid the issue with user run time errors we have try and exception
try:
    age = int(input("Enter your age")) #If the user enters age in letters, this line will giveout an error
except:
    print("The value you have entered is in words. The program needs it to be in numarical data")
    age = int(input("Enter your age"))
#But the above block of code only tries once, if the data is wrong after rety, it'll throw error and exit the code.

if age > 18:
    print(f"Your age is {age}")

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += randint(1, 3)
        new_item += item
        b_list.append(new_item)
    print(b_list)

mutate([1,3,5,8,10])