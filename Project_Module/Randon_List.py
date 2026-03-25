import random

friends = ["Likith", "Deepak Raj", "Shreyas", "Vivek", "Veeresh", "Gaurav"]
#option 1
index = random.randint(0, len(friends))

print(f"The size of list is : {len(friends)}")

print(friends[index-1])# We negated by 1 to adjust index out of range error

#option 2
print(random.choice(friends)) #choise : taKES INPUT AS SEQUENCE. List is one of such sqeuence