import random

score = 0
tries = 0
inans = 0
while tries < 7:

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    print(f"{num1} * {num2} = ?")
    correct = num1 * num2
    human = int(input("answer :"))
    if correct == human:
        print("correct 🎉")
        score += 1


    else:
        print("incorrect answer ❌")
        print(f"the correct answer is {correct}")
        inans += 1

    tries += 1

else:
    print(f"correct answers = {score} ")
    print(f"wrong answers = {inans}")
