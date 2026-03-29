dictionary = {}
print("Welcome to secret oction program!!")
def get_the_winner():
    global dictionary
    control_input = "YES"
    while(control_input != "NO"):
        Name = input("What is your name? ")
        bid_value = int(input("What's the bid"))
        dictionary[Name] = bid_value
        control_input = input("Are there any one else to bid? ").upper()
        if control_input == "YES":
            print("\n" * 100)
    # print(dictionary)

    highest_bid = 0
    Winner = ""
    for names in dictionary:
        # print(names)
        if dictionary[names] > highest_bid:
            highest_bid = dictionary[names]
            Winner = names
    print("\n\n")
    #Print the winner and the amount paied
    print(f"The winner of the bid is \t{Winner} with the bid money of \t{dictionary[Winner]}")

get_the_winner()