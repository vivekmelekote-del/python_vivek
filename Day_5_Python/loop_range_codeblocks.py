#Day 5
#loops
#range
#code blocks
import random
print(range(1, 10))# this will print the range object, not the numbers in the range
print(list(range(1, 10)))# this will print the numbers in the range as a list
print(list(range(1, 10, 2)))# this will print the numbers in the range with a step of 2, starting from 1 and ending before 10
print(list(range(0, 10, 2)))# this will print the numbers in the range with a step of 2, starting from 0 and ending before 10
print(list(range(10, 0, -1)))# this will print the numbers in the range with a step of -1, starting from 10 and ending before 0

# i = 0
# for j in range(1, 101, 1):
#     i += j
# print(i)

for i  in range(1, 101):
    if(((i % 3) == 0) and ((i % 5) == 0)):
        print("FizzBuzz")
    elif((i % 3) == 0):
        print("Fizz")
    elif((i % 5) == 0):
        print("Buzz")
    else:
        print(i)

#One way to generate a password is to use the random module and the string module
print("Welcome to password generator")
length = int(input("Enter the length of the password: "))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
password = ""
for i in range(length):
    password += alphabet[random.randint(0, 51)]# this will add a random alphabet to the password
    password +=numbers[random.randint(0, 9)]# this will add a random number to the password
    password += special_characters[random.randint(0, len(special_characters) - 1)]# this will add a random special character to the password
print("Your password is:", password)

auto_length = random.randrange(4,7)# this will generate a random number between 8 and 16, which will be the length of the password
Password_list = []
for i in range(auto_length):
    Password_list.append(alphabet[random.randint(0, len(alphabet) - 1)])
    Password_list.append(numbers[random.randint(0, len(numbers) - 1)])
    Password_list.append(special_characters[random.randint(0, len(special_characters) - 1)])

# Print either by for loop or by using the join() function
for char in Password_list:
    print(char, end="")# this will print the characters in the password list without a new line
    # print(char, end="")# this will print the characters in the password list without a new line
random.shuffle(Password_list)# this will shuffle the password list
print("Your password is:", "".join(Password_list)) #Converts the list to a string and prints it