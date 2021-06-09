from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like to order ({option}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "admin":
        password = input("Enter the password:")
        if password == "add":
            water = int(input("Add amount of water in ml :"))
            milk = int(input("Add amount of milk in ml : "))
            coffee = int(input("Add amount of coffee in g : "))
            coffee_maker.add_resource(water, milk, coffee)
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)






