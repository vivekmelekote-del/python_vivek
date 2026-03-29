from get_message import init_object
# message_decript = get_message.init()
def comment():
    print("*" * 50)
    print("""Decript the message using Caesar cipher""")
    print("*" * 50)


def decript(encripted_message, shift_count):
    # global message_decript
    message_original = ""
    for i in encripted_message:
        if i in init_object.alphabet:
            message_original += init_object.alphabet[(init_object.alphabet.index(i) - shift_count)]
        elif i in init_object.symbols:
            message_original += init_object.symbols[(init_object.symbols.index(i) - shift_count)]
    
    print("-" * 50)
    print("original message is:\n" + message_original)
    print("-" * 50)
            
            
def start():
    decript(init_object.encripted_message, init_object.shift_count)