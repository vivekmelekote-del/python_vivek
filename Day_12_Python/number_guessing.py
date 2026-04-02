from random import choice


number_of_try = 0
number_list = []
number = 0
end_of_game = False

def choose_number():
    """Randomly gets value from 1 to 100 and return the number"""
    for i in range(1, 101):
        number_list.append(i)
    return choice(number_list)

def choose_difficulty_level():
    """Based on difficulty level, returns the number of try's"""
    difficulty_choice = int(input("Choose the difficulty level by number:\n1. Easy\n2. Medium\n3. Hard\n"))
    if(difficulty_choice == 1):
        return 15
    elif(difficulty_choice == 2):
        return 10
    elif(difficulty_choice == 3):
        return 5

def compare_guess_to_actual_number(number,guess_number):
    """Takes two numbers and check if high or low or same"""
    if(number > guess_number):
        print("Too low\nGuess Again.") 
        return 1
    if(number < guess_number):
        print("Too high\nGuess Again.") 
        return 1
    if(number == guess_number):
        print("Congratulation!!") 
        return 0


print("Welcome to number guessing game!")
print("I'm thinking a number between 1 to 100 \nTry to find out which one")
number = choose_number()
number_of_try = choose_difficulty_level()
while not end_of_game:
    guessed_number = int(input("Make a guess: "))
    successful = compare_guess_to_actual_number(number = number, guess_number = guessed_number)
    number_of_try -= 1
    if successful != 0:
        print(f"You have {number_of_try} attempts remaining to guess the number")
    else:
        end_of_game = True
    if number_of_try == 0:
        print(f"You lost!\nAll the attempts are over\nThe number was {number}") 
        end_of_game = True
