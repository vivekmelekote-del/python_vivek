#Requirement: Write a program to check whether the given number is even or odd, reverse of the number, sum of the digits and also check whether the number is palindrome or not.
from turtle import goto


# import goto
input_num = input("Enter a number: ")#123
rev_num = 0
final_num = 0
total_sun = 0
input_num = int(input_num) 
input_num_copy = input_num 
if(input_num >= 0):
    print("The entered number is Positive")
else:
    print("Enter positive number only")
    exit(0)

if(input_num % 2 == 0):
    print("The entered number is Even")
else:
    print("The entered number is Odd")

while input_num > 0:
    rev_num = input_num % 10
    #3,2,1
    final_num = final_num * 10 + rev_num
    total_sun += rev_num
    #(0*10 + 3) = 3
    #(3*10 + 2) = 32
    #(32*10 + 1) = 321
    # print(final_num)
    input_num = input_num // 10
    # print(input_num)
print("Reverse of the number is: ", final_num)
print("Sum of the digits is: ", total_sun)
if( input_num_copy == final_num):
    print("Palindrome")
else:
    print("Not Palindrome")