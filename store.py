money = 100
while True:
    item = int(input("choose\n 1- Sword = 50\n 2- Shield = 40\n 3- Potion = 10\n 4- CheckMoney\n 5- Exit \n"))
    if item == 1:
        if money < 50:
            print("Not enough money")
        else:
            money -= 50
            print("Sword purchased")

    elif item == 2:
        if money < 40:
            print("Not enough money")
        else:
            money -= 40
            print("Shield purchased")

    elif item == 3:
        if money < 10:
            print("Not enough money")
        else:
            money -= 10
            print("Potion purchased")

    elif item == 4:
        print(f"{money}$")

    elif item == 5:
        break

    else:
        print("Invalid request")
