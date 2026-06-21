import random

temp = random.randint(19, 21)
if temp > 20:
    print("it's hot today make sure that  you drink alot of water ")
elif temp < 20:
    print("it's cold today dress well ")
else:
    print("it's a good day")
# new start
price = 1000000
good_credit = random.choice([True, False])
if good_credit:
    print("you need to put down 10% ")
    print("you have to pay ", price * 10 / 100, "$")
else:
    print("you have to put down 20% ")
    print("you have to pay ", price * 20 / 100, "$")

has_good_income = False
has_good_credit = True
# {and} / {or}  / {not}
if has_good_income or has_good_credit:
    print("you are eligible to ......")

else:
    print("you are not eligible")

name = input("what is your name? \n")
len(name)
if len(name) < 3:
    print("sorry, your name is too short")
    input("enter again ? \n")
elif len(name) > 50:
    print("sorry, your name is too long")
    input("enter again? \n")
else:
    print("your name is perfect")
