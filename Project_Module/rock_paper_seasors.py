import random
import lib_file
print(lib_file.integer_val)
input_num = input("Enter 1: for Rock, 2: for Paper or 3: for Scissors: ")
input_num = int(input_num)
computer_num = random.randint(1,3)
if(computer_num == 1):
    print("Computer chose Rock")
    print(lib_file.rock)
elif(computer_num == 2):
    print("Computer chose Paper")
    print(lib_file.paper)
elif(computer_num == 3):
    print("Computer chose Scissors")
    print(lib_file.scissors)