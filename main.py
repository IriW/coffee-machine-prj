# Coffee Machine
import sys
from art import logo

MENU = {
    1: {
        "item": "espresso",
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    2: {
        "item": "latte",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    3: {
        "item": "cappuccino",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}
resources = {
    "water": 1000,
    "milk": 300,
    "coffee": 100,
}

## Function to get user input for drink choice as well as maintenance (secret option) or resources available.
def get_coin_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == "resources":
        print_resources()
        return None
    elif user_input.lower() == "off":
        sys.exit()
    return int(user_input)
    
    
def resources_sufficient(drink):
    if drink is not None:
        for ingredient in drink["ingredients"]:
            if drink["ingredients"][ingredient] > resources[ingredient]:
                print(f"Insufficient {ingredient}.")
                return False
    return True
def suggest_drink():
    for drink_name, drink in MENU.items():
        if resources_sufficient(drink):
            return drink_name
            # print(f"Insufficient resources. Would you like {drink_name} instead?.")
            # return drink_name
    print("Not enough resources for any drink. Returning money.")
    return None

def deduct_resources(drink):  
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]
    print("Resources deducted.")
    return resources

def print_resources():
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient]}")
    return resources

def process_payment(drink):
    print("Please insert coins. We accept quarters ($0,25), dimes ($0,10), nickels ($0,05). and pennies ($0,01).")
    quarters_pcs = get_coin_input("How many quarters? ")
    if quarters_pcs is None:
        return None
    dimes_pcs = get_coin_input("How many dimes? ")
    if dimes_pcs is None:
        return None
    nickels_pcs = get_coin_input("How many nickels? ")
    if nickels_pcs is None:
        return None
    pennies_pcs = get_coin_input("How many pennies? ")
    if pennies_pcs is None:
        return None

    total_money_inserted = quarters_pcs * COIN_VALUES["quarter"] + dimes_pcs * COIN_VALUES["dime"] + nickels_pcs * COIN_VALUES["nickel"] + pennies_pcs * COIN_VALUES["penny"]
    total_money_inserted = round(total_money_inserted, 2)
    print(f"Total inserted: ${total_money_inserted: .2f}")
    
    if total_money_inserted < drink["cost"]:
        print("Insufficient funds. Money refunded.")
        return None
    return total_money_inserted

is_on = True
print(logo)
while is_on: 
    print("Welcome to the coffee machine!")
    print("Menu:")
    for nr in MENU:
        print(f"{nr}: {MENU[nr]['item']} - ${MENU[nr]['cost']}")

    user_input = input("Please select a drink from the menu. Press '1'. '2', or '3': ").lower()
    if user_input is None:
        continue
    elif user_input == "off":
        is_on = False
    elif user_input == "resources":
        print_resources()
        continue

    try:
        drink_number = int(user_input)
    except ValueError:
        print("Invalid drink number.Please enter '1', '2', '3', or 'resources'.")
        continue
            
    if drink_number not in MENU:
        print("Invalid drink number. Please enter '1', '2', '3', or 'resources'.")
        continue

    drink = MENU[drink_number]
    if not resources_sufficient(drink):
        suggested_drink = suggest_drink()
        if suggested_drink:
            user_response = input(f"Would you like a {suggested_drink} instead? (yes/no): ").lower()
            if user_response == "yes":
                continue # Go back to the beginning of the loop to choose a new drink.
        else:
            print("Returning money.")
            continue

    print(f"Selected drink: {drink['item']}, and the cost is: $ {drink['cost']}")
    
    total_money_inserted = process_payment(drink)
    
    if total_money_inserted is None:
        continue
    elif total_money_inserted == 0:
        print("No money inserted.")
        continue
    elif total_money_inserted < drink["cost"]:
        print("Insufficient funds. Money refunded.")
        continue
    elif total_money_inserted > drink["cost"]:
        change = round(total_money_inserted - drink["cost"], 2)
        print(f"Here is ${change:.2f} in change.")

    deduct_resources(drink)
    print(f"Here is your {drink['item']}. Enjoy!")
    print("Thank you for using the coffee machine.")
    print("===========BYE================")