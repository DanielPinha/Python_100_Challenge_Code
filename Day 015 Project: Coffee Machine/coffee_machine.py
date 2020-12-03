from coffee_machine_database import coffee_recipe, coffee_machine_resource


def prepare_coffee(coffee_choice):
    """prepare selected coffee"""
    resource_missing = check_resource_missing(coffee_choice)
    if resource_missing is not None:
        print(f"Sorry there is not enough {resource_missing}.")
    else:
        quarter = int(input("Please provide number of quarters: "))
        dime = int(input("Please provide number of dimes: "))
        nickel = int(input("Please provide number of nickels: "))
        penny = int(input("Please provide number of quarters: "))
        if check_money(quarter, dime, nickel, penny, coffee_choice):
            machine_adjust_resource(coffee_choice)
            print(f"Here is your {coffee_choice} ☕️. Enjoy!")
            # TODO: Deliver Coffee
    return True


def machine_adjust_resource(coffee_choice):
    """Add coffee cost to machine money and subtract resources"""
    global coffee_machine_resource
    for resource in coffee_machine_resource:
        if resource != 'Money':
            coffee_machine_resource[resource] -= coffee_recipe[coffee_choice]['ingredients'][resource]
        else:
            coffee_machine_resource[resource] += coffee_recipe[coffee_choice]['Cost']


def check_money(quarter_25, dime_10, nickel_5, penny_1, coffee_choice):
    """Check if user money is enough for coffee by return True or False, in case True, provide refund"""
    user_payed = quarter_25 * 0.25 + dime_10 * 0.1 + nickel_5 * 0.05 + penny_1 * 0.01
    if coffee_recipe[coffee_choice]['Cost'] > user_payed:
        print("Not enough money, it will be refunded")
        return False
    else:
        refund = user_payed - coffee_recipe[coffee_choice]['Cost']
        print(f"Here is ${round(refund, 2)} in change.")
        return True


def handle_user_choice(user_choice):
    """Check user input and execute the correct action (function)"""
    if user_choice == 'espresso':
        return prepare_coffee(user_choice)
    elif user_choice == 'latte':
        return prepare_coffee(user_choice)
    elif user_choice == 'cappuccino':
        return prepare_coffee(user_choice)
    elif user_choice == 'report':
        return machine_print_resource()
    elif user_choice == 'off':
        return False
    else:
        print("Invalid command")
        return True


def check_resource_missing(coffee_choice):
    """Receives the coffee choice and check if all resource are available, returns None if all resource are availble
    or the first missing resource"""
    enough_resource = None
    for resource_needed in coffee_recipe[coffee_choice]['ingredients']:
        if coffee_recipe[coffee_choice]['ingredients'][resource_needed] > coffee_machine_resource[resource_needed]:
            enough_resource = resource_needed
            break
    return enough_resource


def machine_print_resource():
    """Print current machine resource available"""
    for resource in coffee_machine_resource:
        print(f"{resource}: {coffee_machine_resource[resource]}")
    return True


machine_should_run = True
while machine_should_run:
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    machine_should_run = handle_user_choice(user_coffee_choice)
