import encript
import decript
from get_message import init


while(True):
    user_input = int(input("1. Encript \n2. Decript \n3.Input a message\n"))
    if user_input == 3:
        init.input_message = input("Enter the message: ")
    if user_input == 1:
        print("HI")
        encript.start()
        # decript.start()
    elif user_input == 2:
        decript.start()
    else:
        print("Wrong choice")
        exit(0)
# user_input = int(input("1. Encript \n2. Decript"))
# if user_input == 1:
#     encript.start()
#     # decript.start()
# else:
#     decript.start()