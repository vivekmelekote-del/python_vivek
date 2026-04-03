#Imports
from game_data import data
from random import randint

#Global variables
random_data = []
dictionary_data = {}
i = 0

def get_random_data():
    """Get a random value from 0 to length of the list 'data'"""
    return randint(0, len(data) - 1)

def print_data(data):
    """Prints the '2' choosen person's information for the player"""
    global i
    if i < 1:
        print(f"Compare A: {data['name']} a {data['description']}, from {data['country']}")
        i += 1
    else:
        print(f"Against B: {data['name']} a {data['description']}, from {data['country']}")

def check_for_followers(list):
    """Checks the 'FOLLOWERS of the '2' celebrities"""
    if((list[0]['follower_count']) > list[1]['follower_count']):
        return 0
    elif((list[1]['follower_count']) > list[0]['follower_count']):
        return 1

def print_follower(list):
    """Prints the followers of '2' celebrities"""
    print(list[0]['follower_count'], list[1]['follower_count'])

def get_data_and_store():
    """Add a information of a celebrity to the list"""
    global i
    random_data.append((data[get_random_data()]))
    print_data(random_data[i])

def congratulate_player(score):
    score += 1
    print(f"Congratulations!!\nThat's right. Your score is: {score}")
    return score

def remove_and_add_data(index):
    """Remove a inrmation of celebrity to list"""
    global i
    i = 0
    random_data.pop(index)
    get_data_and_store()
    print_data(random_data[i])

def highr_or_lower():
    score = 0
    user_wants_to_continue_game = 'y'
    """Game, where user gets to choose who has more followers among the choosen 2 celebrities"""
    random_data.clear()
    get_data_and_store()
    get_data_and_store()
    while(random_data[0] == random_data[1]):
        remove_and_add_data(1)
    continue_game = True
    while continue_game:
        choice = input("Who has more followers? 'a' or 'b' ").lower()
        correct_index = check_for_followers(random_data)
        if(choice == 'a' and correct_index == 0):
            score = congratulate_player(score)
            remove_and_add_data(1)
        elif(choice == 'b' and correct_index == 1):
            score = congratulate_player(score)
            remove_and_add_data(0)
        else:
            continue_game = False
            print(f"Sorry!!\nThat's wrong. Your final score = {score -1}")
    user_wants_to_continue_game = input("Do you want to continue the game??: Y or N").lower()
    return user_wants_to_continue_game


#The program starts from here
continue_game = True
while continue_game:
    i = 0
    if(highr_or_lower() == 'y'):
        continue_game = True
    else:
        continue_game = False