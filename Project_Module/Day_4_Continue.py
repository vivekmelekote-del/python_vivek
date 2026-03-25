#List -> Refer list related function -> https://docs.python.org/3/tutorial/datastructures.html
#Nested list
#Itmes data can be of any data types.
#Systex : Variable = [Item1, Item2, Item3....]{Something like structure}
Fruits = ["Apple", "Banana", "Grape", "Dragon Fruit", "Orange", "Mango", "Sapota"]
for fruit in Fruits:
    print(fruit)

print("Adding new fruit")
Fruits.append("Warwemellen")#append : Add single item at the of llist
print("\n")
for fruit in Fruits:
    print(fruit)

#Not working for some reason. Need more info    
#print("\n")
#for fruit in Fruits:
#    fruit = "Fruit"  
    
print("\n")

for fruit in Fruits:
    print(fruit)
    
    

Fruits.append("Stroberry")
print("\n")

for fruit in Fruits:
    print(fruit)
    
#extend : Adds a list at the end of list
Fruits.extend(["Pine apple", "Cherry", "Pappaya"])
print("\n")

for fruit in Fruits:
    print(fruit)
    
pesticide_list =["Avocados","Sweet corn", "Pineapples", "Cabbages", "Onions","Sweet peas (frozen)", "Papayas", "Asparagus", "Mangoes", "Eggplants", "Honeydew melons", "Kiwis", "Cantaloupes", "Cauliflower", "Broccoli"]
for fruit in pesticide_list:
    print(fruit)
    
print("\n")
print("Combined list is \n")
fruits_pesticide_list = [pesticide_list, Fruits]
for fruit in fruits_pesticide_list:
    print(fruit)
    
    
print(fruits_pesticide_list[1][1])