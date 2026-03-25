import random
print(random.randint(10,150))

import Module_2

print(Module_2.name)
#module
my_fav_num = 3.142

print(random.random()) # value is between 0 and 1 but not including 0 and 1
print(random.random() * 10) 
print(random.uniform(1, 7))# Value between 1 to 7 including 1 and 7

Heads_Tails = random.randint(0, 1) #value is intiger within range including 0 and 1

if Heads_Tails:
    print("Heads")
else:
    print("Tails")