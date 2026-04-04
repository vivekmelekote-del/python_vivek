#OOPs :
#What is Object Oriented Programming? Modeling a real world Object
#How to use OOPs? a Model contains 2 things : What it has (ATTRIBUTES : Variable) and what it does (METHODS : Function).
            #We can create multiple models using something called a CLASS (Blueprint) which could have both attribute ans methods

# Creating object
#Class name has to start with capital letter example "CarBlueprint" C and B like so to differentiate between variables and class.
#car = CarBlueprint()

from prettytable import PrettyTable  #https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
from turtle import Turtle, Screen
turtle_name_is_timmi = Turtle() #Here Turtle is a class and turtle_name_is_timmi is an object created using Turtle() class
screen = Screen()
turtle_name_is_timmi.shape("turtle")
print(turtle_name_is_timmi) #How to use object attributes and methods?
turtle_name_is_timmi.forward(200)
print(turtle_name_is_timmi)
screen.delay(100)
turtle_name_is_timmi.color("green")
print(turtle_name_is_timmi)
print(screen.canvheight) #canvheight is a attribute in Screen class
screen.exitonclick() # is an method in class Screen

table_object = PrettyTable()
print("table_object")
# fruits_dictionay = {}
table_object.add_column("Fruit names" , ["Apple", "Banana", "Chiku", "Dragon fruit", "Grapes", "Fassion fruit"])
table_object.add_column("Colour" ,  ["Red", "Yellow", "Brown", "Red", "Green", "Pink"])
table_object.align = "l"
# table_object.al
print(table_object)
#output
# +---------------+--------+
# |  Fruit names  | Colour |
# +---------------+--------+
# |     Apple     |  Red   |
# |     Banana    | Yellow |
# |     Chiku     | Brown  |
# |  Dragon fruit |  Red   |
# |     Grapes    | Green  |
# | Fassion fruit |  Pink  |
# +---------------+--------+