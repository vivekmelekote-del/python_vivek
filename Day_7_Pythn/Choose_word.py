import sys
# print(sys.path[0])# this will print the current directory
# print(sys.path[1])# this will print the parent directory
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent)) #Add a folder to the top of Python’s search list so imports work from that location first.
import libfile.lib_file as lib_file
list_of_words = ["apple", "Vivek", "Ramyashree", "Pappaya", "Mango", "Family"]
# choosen_word = list_of_words[lib_file.random.randint(0, len(list_of_words) - 1)]
choosen_word = lib_file.random.choice(list_of_words).upper()
#print(choosen_word)
blank_list =[]
count_of_true = 0
count_fo_false = 0
life_list = [lib_file.Sixth_life, lib_file.Fifth_life, lib_file.Fouth_life, lib_file.Third_life, lib_file.Second_life, lib_file.First_life]
# game_over = False

choose_letter = ""#input("Enter a letter: ").upper()
def choose_and_check():# for letter in choosen_word:
    print("In choose_and_check")
    for i in range(0, len(choosen_word)):
        # print(letter)
        if(choosen_word[i] == choose_letter):
            blank_list[i] = choose_letter
            global count_of_true
            count_of_true += 1 #Not needed if we use game_over
    if choose_letter not in choosen_word:
        global count_fo_false
        count_fo_false += 1
    print("".join(blank_list))
    # print(count_fo_false)
    print(life_list[count_fo_false - 1])
    if(count_fo_false == len(life_list)):
        print("Game Over")
        sys.exit()
 

for letter in choosen_word:
    blank_list.append("-")
print("\n")
print("\n")
print("".join(blank_list))
while(count_of_true != len(choosen_word)): #Here we can monitor game_over to exit
    choose_letter = input("Enter a letter: ").upper() 
    choose_and_check()
    #This can also be achived by
    # if "-" not in blank_list:
    #     game_over = True