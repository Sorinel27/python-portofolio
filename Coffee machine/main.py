menu = {
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
storage = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def enough_money(client_money, coffee_type):
    for coffee in menu:
        if coffee == coffee_type:
            for cost in menu[coffee]:
                if cost == 'cost':
                    if client_money < menu[coffee][cost]:
                        return False
    return True


def check_storage(coffee_type):
    is_ok = True
    ingredients = "ingredients"
    water = 'water'
    milk = "milk"
    coffee = "coffee"
    for item in menu:
        if item == coffee_type:
            for ingredient in menu[item]:
                if ingredient == ingredients:
                    for resource in menu[item][ingredient]:
                        if (menu[item][ingredient][resource] > storage[water]) and resource == water:
                            is_ok = False
                            print("Sorry there is not enough water.")
                        elif (menu[item][ingredient][resource] > storage[milk]) and resource == milk:
                            is_ok = False
                            print("Sorry there is not enough milk.")
                        elif (menu[item][ingredient][resource] > storage[coffee]) and resource == coffee:
                            is_ok = False
                            print("Sorry there is not enough coffee.")
    return is_ok


def use_product(coffee_type):
    for item in menu:
        if item == coffee_type:
            for ingredients in menu[item]:
                if ingredients == 'ingredients':
                    for resource in menu[item][ingredients]:
                        storage[resource] -= menu[item][ingredients][resource]


def main():
    money = 0
    cost = 'cost'
    is_ok = True
    while is_ok:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice == 'off':
            return
        elif coffee_choice == 'report':
            for elem in storage:
                if elem == 'coffee':
                    print(f"Coffee: {storage[elem]}g")
                elif elem == 'water':
                    print(f"Water: {storage[elem]}ml")
                elif elem == 'milk':
                    print(f"Milk: {storage[elem]}ml")
            print(f"Money: ${money}")
        elif coffee_choice == 'espresso':
            is_ok = check_storage(coffee_choice)
            if is_ok:
                print("Please insert coins.")
                quarters = int(input("How many quarters?($0.25): "))
                dimes = int(input("How many dimes?($0.10): "))
                nickels = int(input("How many nickels?($0.05): "))
                pennies = int(input("How many pennies?($0.01): "))
                client_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                money_is_ok = enough_money(client_money, coffee_choice)
                if money_is_ok:
                    print(f"Here is ${client_money - money}")
                    print(f"Here is your {coffee_choice} ☕. Enjoy!")
                    use_product(coffee_choice)
                    money += menu[coffee_choice][cost]
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif coffee_choice == 'latte':
            is_ok = check_storage(coffee_choice)
            if is_ok:
                print("Please insert coins.")
                quarters = int(input("How many quarters?($0.25): "))
                dimes = int(input("How many dimes?($0.10): "))
                nickels = int(input("How many nickels?($0.05): "))
                pennies = int(input("How many pennies?($0.01): "))
                client_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                money_is_ok = enough_money(client_money, coffee_choice)
                if money_is_ok:
                    print(f"Here is ${client_money - money}")
                    print(f"Here is your {coffee_choice} ☕. Enjoy!")
                    use_product(coffee_choice)
                    money += menu[coffee_choice][cost]
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif coffee_choice == 'cappuccino':
            is_ok = check_storage(coffee_choice)
            if is_ok:
                print("Please insert coins.")
                quarters = int(input("How many quarters?($0.25): "))
                dimes = int(input("How many dimes?($0.10): "))
                nickels = int(input("How many nickels?($0.05): "))
                pennies = int(input("How many pennies?($0.01): "))
                client_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                money_is_ok = enough_money(client_money, coffee_choice)
                if money_is_ok:
                    print(f"Here is ${client_money - money}")
                    print(f"Here is your {coffee_choice} ☕. Enjoy!")
                    use_product(coffee_choice)
                    money += menu[coffee_choice][cost]
                else:
                    print("Sorry that's not enough money. Money refunded.")


if __name__ == '__main__':
    main()
