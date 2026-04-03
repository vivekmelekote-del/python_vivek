#Expresso   : 50ml water, 18g coffee               : Price - $1.50
#Latte      : 200ml water, 24g coffee, 150ml milk  : Price - $2.50
#Cappuccino : 250ml water, 24g coffee, 100ml milk  : Price - $3.00

# Coffee machine features : 
    # Storage/ contents :300ml water, 200ml milk, 100g coffee
    # Coin operated : Penny - 1 cent, Nickle - 5 cents, Dime - 10 cents, Quarter - 25 cents


#Programming:
    #1. Report            : It needs to report it's relaming contents in the storage
    #2. During order      : When the used order a drink, need to check if resources are sufficient. 
    #3. Money             : Also, ask for user for the money, if ectra, return the change ( Penny, Nickle, Dime, Quarter ). 
        # If not sufficeent money, give feedback. Feedback in $
    #4. During prepration : Deduct the contents of the machine after order is successful
    #5. OFF               : Machine should stop opersting, meaning - Program termination

#Constants
EXPRESSO   = {"Price" : 1.50,
            "usage"   : [50, 18, 0]}

LATTE      = {"Price" : 2.50,
            "usage"   : [200, 24, 150]}

CAPPUCCINO = {"Price" : 2.50,
            "usage"   : [250, 24, 100]}

MACHINE_CONTENT_BACKUP = {"Money"    : 0,
           "storage"  : [300, 100, 200]}

MACHINE_CONTENT = {"Money"    : 0,
           "storage"  : [300, 100, 200]}

def refil():
    """This functions restores MACHINE_CONTENT, inturn restores contents of coffee machine"""
    i = 0
    for i in MACHINE_CONTENT_BACKUP:
        MACHINE_CONTENT[i] = MACHINE_CONTENT_BACKUP[i]

def reduce_the_content(item, money_collected):
    """Reduces the content of coddee machine and adds the money to coffee machine"""
    i = 0
    for items in MACHINE_CONTENT['storage']:
        MACHINE_CONTENT['storage'][i] = items - item[i]
        i += 1
    MACHINE_CONTENT["Money"] += money_collected


def report_function():
    """Reports the contents of coffee machine"""
    print(f"{MACHINE_CONTENT['Money']}$")
    print(f"{MACHINE_CONTENT['storage'][0]}ml")
    print(f"{MACHINE_CONTENT['storage'][1]}g")
    print(f"{MACHINE_CONTENT['storage'][2]}ml")

def take_money():
    """Takes the money from the user for the drink and converts to $ from cents and retrns the money total collected"""
    total = 0
    total += (int(input("How many Quarter?: ")) * 0.25)
    total += (int(input("How many Dime?: "))    * 0.10)
    total += (int(input("How many Nickle?: "))  * 0.05)
    total += (int(input("How many Penny?: "))   * 0.01)
    print("\n" * 10)
    return total

def check_for_sufficient_content(drink):
    """Checks the contents of the achine, retuens 1 if it's enough for the drink else 0"""
    j = 0
    count = 0
    for item in drink:
        if(MACHINE_CONTENT['storage'][j] >= item):
            count +=1
            j += 1
    if count == 3:
        return 1
    else:
        return 0

def ask_for_money_from_user():
    """Returns the money collected"""
    return take_money()

def making_a_drink_collect_money(choosen_drink):
    """Based on the choosen drink, collected money and gives drink when there is sufficient 
    contents to prepare drink and enough money is deposited. 
    Otherwise, informs the user"""
    if check_for_sufficient_content(choosen_drink['usage']):
        money_collected = ask_for_money_from_user()
        if money_collected < choosen_drink['Price']:
            print("Insufficient money collected!\nRefunded")
        elif money_collected == choosen_drink['Price']:
            print("Here is your drink, enjoy")
            reduce_the_content(choosen_drink["usage"], money_collected)
        elif money_collected > choosen_drink['Price']:
            print(f"Here is your remaining change of ${round((money_collected - choosen_drink['Price']), 2)}")
            print("Here is your drink☕, enjoy")
            reduce_the_content(choosen_drink["usage"], choosen_drink['Price'])
    else:
        print("Sorry!!! \nInsifficient content in the machine")

def prepare_drink():
    """Asks for user for drink and based on choice, provides the drink nased on conditions"""
    Key = False
    user_request = int(input("What drink would you like?\n1. EXPRESSO\n2. LATTE\n3. CAPPUCCINO\n\t\t\t"))
    if(user_request == 1):
        making_a_drink_collect_money(EXPRESSO)
    elif(user_request == 2):
        making_a_drink_collect_money(LATTE)
    elif(user_request == 3):
        making_a_drink_collect_money(CAPPUCCINO)
    elif(user_request == 10):
        Key = (int(input()) == 9503)
    else:
        print("Wrong choice of drink!!")
    return Key

end = False
while not end:
    print("\n" *10)
    print("WELCOME!! COFFEE DISPENCER")
    print("PLEASE CHOOSE THE FUNCTION")
    Stop = False
    while not Stop:
        Stop = prepare_drink()
        if(Stop == True):
            print("Under maintainence!")
    if((input("Do you need report?:\n y : yes and n : no: ").lower()) == 'y'):
       report_function()
       refil()
       report_function()
       if((input("Shout down the machine? y : Yes, n : No: ").lower()) == 'y'):
          end = True