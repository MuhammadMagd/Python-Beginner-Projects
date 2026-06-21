num = int(input(">"))
while num != 46 :
    if num > 46 :
        print("lower")
        num = int(input(">"))

    elif num < 46  :
        print("higher")
        num = int(input(">"))

else :
    print ("you won 🎉")

try_num = 3
while try_num > 0 :
    password = input("enter ur password :")
    if password == "Muhammad2009" :
        print("logged in successfully")
        break
    else :
        try_num -= 1
        print ("try again")
else:
    print("Account Locked")

num = int(input("enter : "))
while num > 0 :
    print (num)
    num -= 1
else :
    print ("done")


