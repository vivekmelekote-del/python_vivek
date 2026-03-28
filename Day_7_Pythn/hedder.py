#All the imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent)) #Add a folder to the top of Python’s search list so imports work from that location first.

# This is here, as the above statement has to execute before this statement as, 
# above statement changes OS path to find the file outside this folder
#from libfile.lib_file import health
import libfile.lib_file as lib_file
# print(sys.path[0])# this will print the current directory
# print(sys.path[1])# this will print the parent directory

#List of words to choose from
list_of_words = ["apple", "Vivek", "Ramyashree", "Pappaya", "Mango", "Family"]

#Both statements below will do the same thing
# choosen_word = list_of_words[lib_file.random.randint(0, len(list_of_words) - 1)]
choosen_word = lib_file.random.choice(list_of_words).upper()

blank_list =[]
count_fo_false = 0
life_list = [lib_file.Seventh_life, lib_file.Sixth_life, lib_file.Fifth_life, lib_file.Fouth_life, lib_file.Third_life, lib_file.Second_life, lib_file.First_life]
