#find the largest number in the list, remove duplictes
input_list = [1, 2, 1, 4, 5, 2, 7, 5, 9, 10, 10, 9]
for_revrse = [1, 2, 1, 4, 5, 2, 7, 5, 9, 10, 10, 9]
new_list = []
largest_num = 0
for num in input_list:
    if(num > largest_num):
        largest_num = num
print(largest_num)
i = 0
j = 0
while (i < len(input_list)):
    j = i + 1
    while (j < len(input_list)):
        if(input_list[i] == input_list[j]):
            input_list.pop(j)
        else:
            j += 1
    i += 1
print(input_list)
#Reverse the list
revrselist = for_revrse[7:2:-1] # this will print the numbers in the range with a step of -1, starting from index 7 and ending before index 2
print("Reversed list:", revrselist)

list.reverse(for_revrse) # this revrse function will reverse the list in place and return None
print(for_revrse)
#The below code also reverses.
# for i in range(len(input_list)-1, -1, -1):
#     revrselist.append(input_list[i])

#find the second largest number in the list
second_largest = 0
for num in for_revrse:
    if(num > second_largest and num < largest_num):
        second_largest = num
print("Second largest number is:", second_largest)

#Count the number of odd and even numbers in the list
odd_count = 0
even_count = 0
for list in for_revrse:
    if(list % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
print(f"Odd count is : {odd_count} and Even count is : {even_count}")

#Print
for i in range(2000, 2500):
    if( (i % 4 ) == 0):
        print("Leap year:", i)