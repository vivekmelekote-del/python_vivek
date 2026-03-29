from get_message import init_object
def comment():
    print("*" * 50)
    print("""Encript the message using Caesar cipher""")
    print("*" * 50)

def comment_1():
    print("*" * 50)
    print("""Encripted the message using Caesar cipher""")
    print("*" * 50)

def encript(message, shift):
    comment()
    #Encription code starts from here
    message_to_encript = init_object.encripted_message
    # print("message is: ",message_to_encript)
    # for i in range(0 , 26):
    #     if(alphabet[i] in message):
    #         print(alphabet[i])
    # print("\n")
    for i in message:
        # print(i)
        if i in init_object.alphabet:
            a = init_object.alphabet.index(i) + shift
            print(i)
            if a > 26:
                a = a - 52
            init_object.encripted_message += init_object.alphabet[a]
        elif i in init_object.symbols:
            print(i)
            a = init_object.symbols.index(i) + shift
            if a > 30:
                a = a - 30
            init_object.encripted_message += init_object.symbols[a]
    comment_1()
    print("-" * 50)
    print("Encripted message is: " + init_object.encripted_message)
    print("-" * 50)
        
def start():
    encript(init_object.input_message, init_object.shift_count)