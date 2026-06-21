import random
while True :
        player = input ("{rock / paper / scissors} :")

        if player == "exit"  :
            break

        if player not in ["rock" , "scissors" , "paper"] :
            print ("invalid choice")
            continue
        else :
            computer = random.choice(['rock', 'paper' , 'scissors'])
            print (player, "VS" ,  computer)
            if player == computer :
                print ("draw")
            elif player != computer :
                if player == "rock" and  computer == "paper" or player == "scissors" and  computer == "rock" or player == "paper" and  computer == "scissors" :
                    print ("you lost 😂")
                if player == "paper" and  computer == "rock" or  player == "rock" and  computer == "scissors" or player == "scissors" and  computer == "paper" :
                    print ("you won 🎉")