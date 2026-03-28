import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import libfile.lib_file as lib_file
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

if(input_num == computer_num):#if both are same, it's a tie
    print("It's a tie")
elif(input_num == 1 and computer_num == 3):#Rock beats scissors
    print("You win")
elif(input_num == 2 and computer_num == 1):#Paper beats Rock
    print("You win")
elif(input_num == 3 and computer_num == 2):#Scissors beats Paper
    print("You win")
else:
    print("Computer wins")