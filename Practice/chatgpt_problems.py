#find the largest number in the list, remove duplictes
input_list = [1, 2, 1, 4, 5, 2, 7, 5, 9, 10, 10, 9]
new_list = []
largest_num = 0
for num in input_list:
    if(num > largest_num):
        largest_num = num
# print(largest_num)
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
for num in input_list:
    print(f"list is : {num}")