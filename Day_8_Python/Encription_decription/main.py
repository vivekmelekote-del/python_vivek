import encript
import decript


while(True):
    user_input = int(input("1. Encript \n2. Decript"))
    if user_input == 1:
        print("HI")
        encript.start()
        # decript.start()
    else:
        decript.start()
# user_input = int(input("1. Encript \n2. Decript"))
# if user_input == 1:
#     encript.start()
#     # decript.start()
# else:
#     decript.start()