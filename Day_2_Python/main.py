# print("Hello!, \n" + "Welcome to brand name generator\n")
# city_name = input("Enter the city you are from\n")
# pet_name = input("Enter your pet name\n")
# print("YOUR BAND NAME COULD BE \n" + city_name + " " + pet_name)


print("Hello"[0])#output is 'H'
print("Hello"[4])#Output is 'o'
print("Hello"[-1])#Output is 'o'
print(123+123)#Adds the 2 number where "123" + "123" just combines both considering as basestring
print(100_000)#here _ is ignored and prints 100000
print(100_000 + 1000) #output is 101000, here they are both considered as munbers andd sums the number
#len() function can't take int value, or any number
#Boolean 1. True 2. False, starting with capital latter
print(type("vivek")) #type() function gives out the datatype of the data
print(type(123))
print(type(1.5))
print(type(False))

#------------------------mathametical operator-------------------------#

print(int("123") + int("123")) #type conversion
# print("Number of letters in you name: " + str(len(input("Enter your name "))))
print(6 / 2) #output is 3.0
print(6 // 2)#output is 3
print(2 ** 3)# power 2 power 3, so output is 8
# PEMDAS -> (), exponent, *, /, +, -
print(3 * 3 + 3 / 3 - 3) #(3 * 3) + (3 / 3) - 3
print(3 * (3 + 3) / 3 - 3)


#-------------------------------------------------#
bmi = ( 84 / 1.65 ** 2)
print(bmi)
print(round(bmi)) # reound() it gives closest rounf number for a float number
print(round(bmi, 2)) # the 2 is, it gives 2 digits after decimal


#-----------------------Assignment operator--------------------------#
score = 0
score += 1
print("Your score id :" + str(score))

#-----------------------fstring--------------------------#

print(f"Your score id :{score}, \nyour bmi is: {bmi}")

#-----------------------Example program--------------------------#
print("Welcome to tip calculator!")
bill_amount = float(input("What was the total bill\n"))
# print(type(bill_amount))
tip_percentage = int(input("How much tip would you loke to pay? 10. 12 or 15\n"))
headcount = int(input("How many people to split the bill?\n"))
Individual_cost = (((bill_amount) + ((bill_amount * tip_percentage)/100)) / headcount)
print(round(Individual_cost, 2))

#----------------------------------------------------------------#