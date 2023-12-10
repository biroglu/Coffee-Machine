water = 400
milk = 540
coffee_beans = 120
disp_cups = 9
money = 550




def current_state():
    print("The coffee machine has:\n"
          + str(water) + " of water\n"
          + str(milk) + " of milk\n"
          + str(coffee_beans) + " of coffee beans\n"
          + str(disp_cups) + " of disposable cups\n"
          + str(money) + " of money")


def espresso():
    global water, coffee_beans, money, disp_cups

    if water >= 250 and coffee_beans >= 16 and disp_cups >= 1:
        print("I have enough resources, making you a coffee!")
        water -= 250
        coffee_beans -= 16
        money += 4
        disp_cups -= 1
        
        
    elif water < 250:
        print("Sorry, not enough water!")
    elif coffee_beans < 16:
        print("Sorry, not enough coffee beans!")
    elif disp_cups < 1:
        print("Sorry, not enough disposable cups!")


def latte():
    global water, milk, coffee_beans, money, disp_cups

    if water >= 350 and milk >= 75 and coffee_beans >= 20 and disp_cups >= 1:
        print("I have enough resources, making you a coffee!")
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        disp_cups -= 1
    elif water < 350:
        print("Sorry, not enough water!")
    elif  milk < 75:
        print("Sorry, not enough milk!")
    elif coffee_beans < 20:
        print("Sorry, not enough coffee beans!")
    elif disp_cups < 1:
        print("Sorry, not enough disposable cups!")


def cappuccino():
    global water, milk, coffee_beans, money, disp_cups

    if water >= 200 and milk >= 100 and coffee_beans >= 12 and disp_cups >= 1:
        print("I have enough resources, making you a coffee!")
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        disp_cups -= 1

    elif water < 200:
        print("Sorry, not enough water!")
    elif milk < 100:
        print("Sorry, not enough milk!")
    elif coffee_beans < 12:
        print("Sorry, not enough coffee beans!")
    elif disp_cups < 1:
        print("Sorry, not enough disposable cups!")


def back():
    return None


def buy():
    buy_state = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

    if buy_state == "1":
        espresso()
    elif buy_state == "2":
        latte()
    elif buy_state == "3":
        cappuccino()
    elif buy_state == "back":
        back()


def fill():
    global water, milk, coffee_beans, disp_cups

    fill_water = int(input("Write how many ml of water do you want to add:"))
    fill_milk = int(input("Write how many ml of milk do you want to add:"))
    fill_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add:"))

    water += fill_water
    milk += fill_milk
    coffee_beans += fill_beans
    disp_cups += fill_cups


def take():
    global money
    print("I gave you $" + str(money))
    money -= money


def remaining():
    current_state()

while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        break
