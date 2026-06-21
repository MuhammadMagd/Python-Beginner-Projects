balance = 1000

while True:

    request = input(
        "What is your request?\n"
        "{check balance / deposit / withdraw / exit} : "
    ).lower()

    if request == "check balance":
        print(f"Your balance is {balance}$")

    elif request == "deposit":

        plenty = int(input("How much do you want to deposit? : "))

        if plenty < 0:
            print("Can't do this")

        else:
            balance += plenty
            print(f"Deposit successful")
            print(f"Your balance is {balance}$")

    elif request == "withdraw":

        lack = int(input("How much do you want to withdraw? : "))

        if lack < 0:
            print("Can't do this")

        elif lack > balance:
            print("Sorry, insufficient balance")

        else:
            balance -= lack
            print("Withdraw successful")
            print(f"Your balance is {balance}$")

    elif request == "exit":
        break

    else:
        print("Invalid request")
