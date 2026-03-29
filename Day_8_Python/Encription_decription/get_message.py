from random import randint

#Get the message from user to encript
# class init_data:
class init():
    input_message = input("Enter the message: ")#.upper()
    # user_input = input("Enter \nENCODE\nDECODE\nCONTINUE ")

    #Alphabee list to take reference for encription
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    #Symbols list to take reference for encription
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/', ' ']

    #Get the position to shift the letter from reference
    # shift_count = int(input("Enter the shift count: "))
    shift_count = randint(1, 15)
    print(shift_count)
    
    encripted_message = ""



    # a = alphabet.index(input_message)
    # a += shift_count
    # if a > 26:
    #     a = a - 26
    # print(alphabet[a - 1])

#create an object
init_object = init()