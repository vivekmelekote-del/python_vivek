#Conditional statements, logical operators, code blocks and scope#
#---------------Conditional statements-------------------#
print("Welcome to rollercoaster! :)")
hight = float(input("What's the player hight in cm: "))

if hight >= 128:
    print("Continue to the ride :)")
else:
    print("Sorry!, You can't ride :(")
    
    
#---------------- % operator -------------------#
print(10 % 3)

input_number = int(input("Enter the number to find is it ODD or EVEN: "))
if input_number % 2 == 0:
    print("Enev number")
else:
    print("Odd number")
#------------------- Nested if and elif-------------------#
print("Welcome to rollercoaster! :)")
hight = float(input("What's the player hight in cm: "))
age = int(input("Enter the player age :"))

if hight >= 128:
    if age <=12:
        print("Ticket price is 50Rs")
    elif age <= 18:
        print("Ticket price is 70Rs")
    else:
        print("Ticket price is 120Rs")
else:
    print("Sorry!, You can't ride :(")
    
#------------------- Pizza project -------------------#
print("Welcome to pizza deliveries!")
size = input("What size of pizza do you want? S M L. ")
pizza_cost = 0
if size == 'S' or size == 's':
    pizza_cost = 15
elif size == 'M' or size == 'm':
    pizza_cost = 120
elif size == 'L' or size == 'l':
    pizza_cost = 20
else:
    print("You selected invalid size of pizza")
    exit(0)

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if (pepperoni == "Y" or pepperoni == "y") and size == "s":
    pizza_cost += 2
elif (pepperoni == "Y" or pepperoni == "y") and size != "s":
    pizza_cost += 3
elif pepperoni != "N" and pepperoni != "n":
    print("You selected invalid option!" + pepperoni)
    exit(0)

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y" or extra_cheese == 'y':
    pizza_cost += 1
elif pepperoni != "N" and pepperoni != "n":
    print("You selected invalid option!")
    exit(0)
    
print(f"total const of pizza is : {pizza_cost} $")
#------------------- Logical operator -------------------#
# and, or, not
#below both code is correct whay to write conditional operator
a = 10
b = 20
c = 30
if a > b and a > c:
    print("a is greater")
elif b > c and b > a:
    print("b is greater")
else:
    print("c is greater")
    
a = 10
b = 20
c = 30
if c < a > b:
    print("a is greater")
elif a < b > c:
    print("b is greater")
else:
    print("c is greater")
    
    
    
#------------------- Fun Game, Finding a treasure -------------------#
# ''' in print suggest compiler there are multiple lies of strigs or multi block strig.
# "" diesnt work for this cases

#DESIGNS CAN BE FOUND IN THIS URS : https://ascii.co.uk/art
print('''
        *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to FIND THE TREASURE game! \n\n")
continue_hunt = ""
Boat = ""
road = input('You\'re at a jusction.\n Would you loke to go "Stright", "right" or "left"? ')
#Importent \ occurs infront of useful symbol, it'll mean, it'll suggest compiler 
#dont inturprit as code
if road == "Stright" or road == "stright":
    print("Reached train station")
    print('''
                                                     __   __
                                                 /'   `\
                                                Y.     .Y
                                      _______    \`. .'/
                       ,-------------'======="--""""-""""---.
                 __,=+'-------------------------------------|p
              .-/__|_]_]  :"/:""""""""""""""""""""""""""""""|'
           ,-'__________[];/_;_____________________T G V____|
         ,".../_|___________________________________________|
        (_>        ,-------.                     ,-------.  |
         `-._____.'(_)`='(_)\_7___7___7___7__7_.'(_)`='(_)\_/''')
    train = input("Would you like to explore or board a train? YES or NO ")
    if train == "YES" or train == "yes":
        print("train met with accident, you loose!!!!!")
    elif train == "NO" or train == "no":
        print("You found a treasure map while exploring!")
        print('''
          ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')
        continue_hunt = input("Would you like to continue to find treasure? Yes ot No ")
if continue_hunt == "Yes" or continue_hunt == "yes" or road == "left" or road == "Left":
    print("Reached lake")
    Boat = input("Wait for boat or swim accross lake? Yes or No: \n")
    if Boat == "Yes" or Boat == "yes":
        print("Explore the highland")
        print("....................\n........................\n..........................\n")
        print("Found a treasure")
    else:
        print("Game over, eaten by crockodile!!!")

        print('''                        .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-' ''')
                                   
elif road == "right" or road == "Right":
    print("Accedent, lost the game!!!!!!!!!!!")
    print('''
              _                                                       _
     / \                                                     / \
     )_(                                                     )_(
      |            _________________________________________  |
      |      _____|.-----..-----..-----..-----..----..-----.] |      
      |     /.--.|||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;|| |
      |    //   ||||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;|| |
  ___...--'|`---'|||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;|| |
 (=      | |   -'|||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;||_|__
 |  _..--' |____.'||;;;;;||;;;;;||;;;;;||;;;;;|'----'|;;;;;||____|
 |-'.----.  _____ |'-----''-----''-----''-----'.----.'-----'|.....
|=./ .--. \|=====||___________________________/ .--. \______] 
'=' :(--): `-----''--------------------------' :(--): `-----'   
.... `--' ..................................... `--' ..LGB........
===================\\\\==========================================''')