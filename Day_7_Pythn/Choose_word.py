from sys import exit
from hedder import choosen_word, blank_list, count_fo_false, life_list
choose_letter = ""#input("Enter a letter: ").upper()
def choose_and_check():# for letter in choosen_word:
    for i in range(0, len(choosen_word)):
        if(choosen_word[i] == choose_letter):
            blank_list[i] = choose_letter

    #When the player guesses the wrong letter, he looses an life
    if choose_letter not in choosen_word:
        global count_fo_false
        count_fo_false += 1
    print("".join(blank_list))

    #When the player guesses all the letter in the word, exit the game
    if("-" not in blank_list):
        print("CONGRATULATIONS!!!")
        print("*************************************You win*************************************")
        exit()

    #Print the hangman ascii art based on the number of wrong guesses
    print(life_list[count_fo_false])

    #When player looses all this chances, exit the game
    if(count_fo_false == (len(life_list) - 1)):
        print("The word was " + choosen_word)
        print("*************************************Game Over*************************************")
        exit()
 
# first print blanks to find number of letter the word has
for letter in choosen_word:
    blank_list.append("-")
print("".join(blank_list))

def check_repeat():
    if choose_letter in blank_list:#If player enters same letter, say that letter is already guessed
        print("You have already guessed this letter")
        return False
    return True

while(True): #Here we can monitor game_over to exit
    choose_letter = input("Enter a letter: ").upper() 
    if(check_repeat()):
        choose_and_check()