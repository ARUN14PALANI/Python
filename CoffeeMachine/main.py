MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

print(MENU["latte"]["ingredients"]["water"])
print(resources["water"])
machine = "on"


def flavor_water(selected_flavour):
    return MENU[selected_flavour]["ingredients"]["water"]


def flavor_milk(selected_flavour):
    return MENU[selected_flavour]["ingredients"]["milk"]


def flavor_coffee(selected_flavour):
    return MENU[selected_flavour]["ingredients"]["coffee"]


def add_to_wallet(collected_amounts):
    resources["money"] += collected_amounts


def reduce_resources(flavour_water, flavour_milk, flavour_coffee):
    resources["water"] -= flavour_water
    resources["milk"] -= flavour_milk
    resources["coffee"] -= flavour_coffee


def convert_to_dollar(coin_q, coin_d, coin_p, coin_n):
    coin_q = coin_q * 0.25
    coin_d = coin_d * 0.10
    coin_p = coin_p * 0.05
    coin_n = coin_n * 0.01
    dollar_amount = [coin_q, coin_d, coin_n, coin_p]
    return sum(dollar_amount)


def display_amount(selected_flavour):
    return MENU[selected_flavour]["cost"]


def check_availability(selected_flavour):
    availability_status = ""
    for ingredient in MENU[selected_flavour]["ingredients"]:
        if ingredient == "water":
            if MENU[selected_flavour]["ingredients"][ingredient] > resources[ingredient]:
                print(f"There is no enough {ingredient}")
                availability_status = "no"
                return availability_status
            else:
                availability_status = "yes"
        elif ingredient == "milk":
            if MENU[selected_flavour]["ingredients"][ingredient] > resources[ingredient]:
                print(f"There is no enough {ingredient}")
                availability_status = "no"
                return availability_status
            else:
                availability_status = "yes"
        elif ingredient == "coffee":
            if MENU[selected_flavour]["ingredients"][ingredient] > resources[ingredient]:
                print(f"There is no enough {ingredient}")
                availability_status = "no"
                return availability_status
            else:
                availability_status = "yes"

    return availability_status


while not machine == "off":
    flavour = input("What would you like? (espresso/latte/cappuccino): ")
    flavour = flavour.lower()
    if flavour == "off":
        machine = "off"
    elif flavour == "report":
        print(resources)
    else:
        print(flavour)
        if check_availability(flavour) == "yes":
            print("available")
            flavour_value = float(display_amount(flavour))
            print(f"value of {flavour} is $ {flavour_value}/-")
            print("Please insert coins!")
            quarters = float(input("how many quarters?"))
            dimes = float(input("how many dimes?"))
            pennies = float(input("how many pennies?"))
            nickels = float(input("how many nickels?"))
            inserted_amount = convert_to_dollar(quarters, dimes, pennies, nickels)
            print(f"Inserted total amount is {inserted_amount:.2f}")
            if inserted_amount >= flavour_value:
                balance = inserted_amount - flavour_value

                if balance > 0:
                    print(f"Here is your change $ {balance:.2f}")
                print(f"Here is your{flavour}, enjoy!")
                add_to_wallet(flavour_value)
                if flavour == "espresso":
                    reduce_resources(flavor_water(flavour), 0, flavor_coffee(flavour))
                else:
                    reduce_resources(flavor_water(flavour), flavor_milk(flavour), flavor_coffee(flavour))

            else:
                print("Sorry!, there is no enough money!, your amount is refunded")

        else:
            print("sorry!")
