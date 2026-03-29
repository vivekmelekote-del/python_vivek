# def greeting(name, location):
#     print(f"Hello {name}")
#     print(f"I'm from {location}")
# def greeting(name, location, day):
#     print(f"Hello {name}")
#     print(f"I'm from {location}")
#     print(f"Today is a {day}")
    
list1 = ["Vivek", "Bengaluru", "Crazy day", "Python is fun", "I love coding"]

# greeting("Vivek", "Bengaluru") #This is a simple function using positional arguments. We can also use keyword arguments to call the function like this:
# greeting(location="Bengaluru", name="Vivek")
# greeting("Vivek", location="Bengaluru") #We can also mix positional and keyword arguments, but the positional arguments must come before the keyword arguments. This will work fine.

#Extra information about function arguments:
#Some of there dont' work. Need to check them out and understand them better.
# greeting(name="Vivek", "Bengaluru") #This will give an error because the positional argument is after the keyword argument. We need to change it to:
# greeting("Vivek", name="Vivek") #This will work fine because the positional argument is before the keyword argument.
# greeting("Vivek", "Bengaluru", "Crazy day") #This will work fine because we have provided all the required arguments. If we try to call the function without providing all the required arguments, we will get an error like this:
# greeting("Vivek", "Bengaluru") #This will give an error because we have not provided the required argument 'day'. We can fix this by providing a default value for the 'day' parameter like this:
# def greeting(name, location, day="a good day"):
#     print(f"Hello {name}")
#     print(f"I'm from {location}")
#     print(f"Today is {day}")

print("\n\n\n")

# ============================================================================
# LESSONS LEARNT - GLOBAL VARIABLES AND STATE MANAGEMENT
# ============================================================================
# PROBLEM FOUND: When calling the function multiple times, the results were 
# accumulating instead of giving fresh calculations.
#
# ROOT CAUSE:
# 1. Global variable 'count' was initialized as empty list [] instead of 
#    [0, 0, 0, 0, 0, 0, 0, 0] (8 zeros for t,r,u,e,l,o,v,e letters)
#
# 2. Variables 'name_list' and 'count' were NOT being reset/cleared inside 
#    the function. This caused:
#    - First call: Vivek + Bengaluru = 54% ✓ (correct)
#    - Second call: names accumulated + counts accumulated = 352% ❌ (wrong, should be 13%)
#    - Third call: even more accumulated = 540% ❌ (wrong, should be 44%)
#
# 3. With each function call, old data was never cleared, so scores kept 
#    adding up: 208%, 352%, 540%, 740%, 974% (all wrong!)
#
# SOLUTION:
# Added two reset lines at the START of calculate_love_score() function:
#    name_list.clear()              # Clear old names from previous calls
#    count = [0, 0, 0, 0, 0, 0, 0, 0]  # Reset count array to all zeros
#
# KEY LEARNING:
# When using global variables, ALWAYS reset them inside functions if they 
# might be called multiple times. Otherwise, old data will persist and cause 
# bugs that are hard to find!
# ============================================================================

name_list = []
count = [0, 0, 0, 0, 0, 0, 0, 0]  # Initialize with 8 zeros, not empty list
# i = 0
# j = 0
# k = 0
def calculate_love_score(name1, name2):
    global count, name_list
    
    # CRITICAL: Reset global variables for FRESH calculation each time
    # Without this, values from previous calls would accumulate!
    # Example of the bug: First call returned 54%, second call returned 208% 
    # instead of 13% because count array still had old values
    name_list.clear()  # Remove names from previous function calls
    count = [0, 0, 0, 0, 0, 0, 0, 0]  # Reset all counts to zero
    
    i = 0
    j = 0
    k = 0
    list2 = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']
    name_list.append(name1)
    name_list.append(name2)
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    for name in name_list:
        for i in range(0, len(list2)):
            count[i] += find_letters(name, list2[i])
        # print(count)
        # print("\n\n")
    i = 0
    j = 1
    while(j <= 2):
        while(i < (4*j)):
            k += count[i]
            i += 1
        if(j == 1):
            k *= 10
        j += 1
        # print(i , j, k)
    # print(f"Your love score is {k}%")
    return k


def find_letters(name, letter):
    count = 0
    for letter_in_name in name:
        if(letter == letter_in_name):
            count += 1
    return count

# input_name1 = input("Enter your name: ")
# input_name2 = input("Enter your partner's name: ")
# calculate_love_score(input_name1, input_name2)
calculate_love_score("Kanye West", "Kim Kardashian")