#Day 5
#loops
#range
#code blocks
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