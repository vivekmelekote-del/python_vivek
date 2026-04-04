from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_class = Menu()
coffeemaker_class = CoffeeMaker()
money_machine_class = MoneyMachine()
# while
is_sufficient_resources = False
choice = False
while choice != True:
    user_drink_choice = input(f"Select from the menu, which dring would you like to have?: {menu_class.get_items()}").lower()
    if(user_drink_choice == "latte" or user_drink_choice == "espresso" or user_drink_choice == "cappuccino"):
        is_sufficient_resources = coffeemaker_class.is_resource_sufficient(menu_class.find_drink(user_drink_choice))
        if(is_sufficient_resources):
            money_machine_class.make_payment(menu_class.find_drink(user_drink_choice).cost) # The return of find drink will be a list, then we pass cost alone to paymeny
            coffeemaker_class.make_coffee(menu_class.find_drink(user_drink_choice))
    elif(user_drink_choice == "stop"):
            choice = True
    elif(user_drink_choice == "report"):
            coffeemaker_class.report()
            money_machine_class.report()
    else:
          print("Wrong choice")