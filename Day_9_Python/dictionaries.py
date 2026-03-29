#Dictionary syntex : 
#Dictionary_name = {key1 : Value1, Key2 : value2, Key3 : value3, .......}
Programming_dictionay = {
    "bug" : "Error in code",
    "function" : "Block of instructions that perform a action",
    "Loop" : "A action of someting that ecevutes multiplt times",
    }
print(Programming_dictionay["bug"]) #prints  only bug
Programming_dictionay["variable"] = "Used to hold a value to be used in the code"

print(Programming_dictionay) #prints the coplete dictionay

Programming_dictionay["Bug"] = "An error in code that prevents normal execution of the program" #Here we are updating the data on the dictionary
print(Programming_dictionay["Bug"])

#Looping through dictionay
for i in Programming_dictionay:
    print(i) #But it only prints the Key rather than entire ot value of the dictioany

for i in Programming_dictionay:
    print(Programming_dictionay[i]) #Here prints the value of the dictioany

Programming_dictionay = {} #This kind of cleares all data in the dictionay
print(Programming_dictionay)

print("*" * 50)
print(" " *20 + "Nested" + " " * 15)
print('''
    dictionary_1 = {"Key1" : [list],
                    "Key2" : {Dictionary2},
                    ...}
        ''')
print("*" * 50)


country_capital = {"India" : "Delhi",
                   "Germany" : "Berlin",
                   "Sweden" : "Stockholm",
                   }

#Nested dictionay with lists
travel_log = {"India" : ["Bengaluru", "Hampi", "Maysur"],
              "Germany" : ["Hamburg", "Munich", "Cologne", "Frankfurt"],
              "Sweden" : ["Göteborg", "Malmö", "Uppsala"],
              }

print("Accessing a value of key and finding second value in the lisy of values: ",travel_log["India"][1]) # Hampi

#Nested dictionaries
travel_log = {"India" : {"cities_visited" : ["Bengaluru", "Hampi", "Maysur"],
                        "number_of_times_visited" : 3},
              "Germany" : {"cities_visited" : ["Hamburg", "Munich", "Cologne", "Frankfurt"],
                        "number_of_times_visited" : 0},
              "Sweden" : {"cities_visited" : ["Göteborg", "Malmö", "Uppsala"],
                        "number_of_times_visited" : 2},
              }

print("Getting data from nested dictionary: ",travel_log["India"]["number_of_times_visited"])
print("*" * 10)
print("Now lets loop through nested list")
print("*" * 10)

for key in travel_log:
    for key2 in travel_log[key]:
        print(travel_log[key][key2])

print("*" * 10)


list1 = ['a', 'b', ['c', 'd']]
#This is same as 2X2 matrix
#  _                      _
# | a                    b |
# |_c                    d_|
print("Accessing data in a nested list: ",list1[2][0])


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2]) #This will print complete list ["Steak"]
print(order["main"][2][0]) #This will print "Steak", a member of list