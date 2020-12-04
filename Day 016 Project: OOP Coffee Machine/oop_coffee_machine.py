from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_money_handler = MoneyMachine()
coffee_maker = CoffeeMaker()

machine_should_run = True
while machine_should_run:
    available_items = coffee_menu.get_items()
    choice = input(f"What would you like? {available_items} ")
    if choice == 'report':
        coffee_maker.report()
        coffee_money_handler.report()
    elif choice == 'off':
        machine_should_run = False
    elif coffee_menu.find_drink(choice):
        drink = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and coffee_money_handler.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

