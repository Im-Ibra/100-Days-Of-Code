from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m_machine = MoneyMachine()
c_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        c_maker.report()
        m_machine.report()
    else:
        drink = menu.find_drink(choice)
        if c_maker.is_resource_sufficient(drink) and m_machine.make_payment(drink.cost):
            c_maker.make_coffee(drink)