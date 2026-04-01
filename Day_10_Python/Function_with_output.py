#Functions with output
#Docstrings : Used to create a documents as we go along in functions or blocks of code. It has to be filst line after the function defnition.

#Function to make only first letter in a word capital. Title function.
def format_name(First_name, Second_name):
    #The below is a comment
    # """This is a title function"""    #This can be multi line
    
    #The below is docstring
    """This function makes the first letter
    as capital latter and puts data in a list and returns"""
    First_name = First_name.title()
    Second_name = Second_name.title()
    return [First_name, Second_name] #Here we are returning a list. So, we are returning multiple variable as a truen from a function.

name_list = {"Name1" : "Shreyas"}   
print(type(name_list)) #Here it's dictionary
#name_list = format_name("VIVEK", "VENAKATESH") #Collecting the return value and storing in a list as the output is list. Irrespective of what type of variable is used to store data, it'll be converted to list
name_list = format_name("VIVEK", "VENAKATESH")
print(name_list)
print(type(name_list))#Here it's list. Beacuse we have not given the Ket when storing th data in the dictionary. Then, it overwrites the data to list.


# Calculatro project : Refer Day_6_Python\Function_Codeblocks_While_loop