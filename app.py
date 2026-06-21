import random

weight = input( " Enter your weight: \n ")
weight = float(weight)
print("≃" , weight * 0.45359237 , "KG")
course = '''
hi muhammad,
it's me from the past
I'm so proud of you
❤️
'''
print(course)
[0 / 1 / -1 ]
name = 'jeffry'
print(name [1:-1])
first = "mia"
last = "Doe"
msg = f'{first} [{last}] is a coder '
print(msg)
course = "python"
print (len(course))
print (course.upper())
print (course.title())
print (course.replace("python","programming"))
"...." in variable
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 ** 3)
x = 10
x = x + 3
x +=  3
x -=  3
print(x)
x=2.9
print(round(x))
print(abs(x)) #abslute value always positive

temp = random.randint(1,50)
if temp > 30 :
    print("it's a hot day")
elif temp <10 :
    print("it's a cold day")
else :
    print("it's neither hot or cold")

name = input("what is your name? \n")
len(name)
if len(name) < 3:
    print("sorry, your name is too short")
    input("enter again ? \n")
elif len(name) > 50:
    print("sorry, your name is too long")
    input("enter again? \n")
else :
    print ("your name is perfect")

weight = float(input("weight :  "))
unit = input("unit  (K)g or (L)bs  ").lower()

if unit == "k"  :
    print (weight * 2.20462 , "pounds")
else:
    print (weight / 2.20462 , "kilograms")

repeat = input("repeat (y/n)? ")
if repeat == "y" :
    weight = float(input("weight :  "))
    unit = input("unit  (K)g or (L)bs  ").lower()
    if unit == "k":
        print(weight * 2.20462, "pounds")
    else:
        print(weight / 2.20462, "kilograms")
i = 1
while i <= 5 :
    print ( "*" * i)
    i = i + 1
print ("done")
