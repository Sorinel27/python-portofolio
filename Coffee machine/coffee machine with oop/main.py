from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


def main():
    is_ok = True
    while is_ok:
        coffee_choice = input(f"What would you like? ({menu.get_items()}): ")
        if coffee_choice == 'off':
            is_ok = False
        elif coffee_choice == 'report':
            print(coffee.report())
            print(money.report())
        else:
            drink = menu.find_drink(coffee_choice)
            if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)


if __name__ == '__main__':
    main()
