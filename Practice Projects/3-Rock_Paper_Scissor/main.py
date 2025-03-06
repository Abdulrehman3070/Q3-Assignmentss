import random
#Rules
# Players simultaneously form a rock, paper, or scissors shape with their hands.
# Rock beats scissors, scissors beats paper, and paper beats rock. 
# If both players choose the same shape, the round is a tie. 
# The game is often replayed until there is a winner. 
options=["rock", "paper","scissor"]
computer_wins=0 
user_wins=0
rounds  =0

Greet = "Welcome to my Computer Game!"
playing = input(f"""{Greet}
Do You Want to Play rock-paper-scissor? (yes/no) : """)

if playing.lower() == "yes":
    while rounds<5:
            random_value = random.choice(options)
            rounds+=1
            print(f"Round {rounds}: ")
            my_value = input("Your Turn : ")
            my_value = my_value.lower()
            if my_value == options[0] or my_value == options[1] or my_value == options[2]:
                if (my_value == "rock" and random_value == "scissor") or (my_value == "scissor" and random_value == "paper") or (my_value == "paper" and random_value == "rock") :
                    user_wins+=1
                    print(f"User win Round{rounds}!")
                elif (my_value == "scissor" and random_value == "rock") or (my_value == "paper" and random_value == "scissor") or (my_value == "rock" and random_value == "paper"):
                    computer_wins+=1
                    print(f"Computer win Round{rounds}!")
                elif my_value == random_value:
                    print("its a tie")
            else:
                print("Write Correct Spellings") 
                rounds-=1

    if user_wins>computer_wins:
        print(f"User win with {user_wins}:{computer_wins}")
    elif computer_wins>user_wins:
        print(f"Computer win with {computer_wins}:{user_wins}")
    elif computer_wins==user_wins:
        print(f"Game Draw {computer_wins}:{user_wins}")
    
else:
    print("Okay , Have a Nice Day Ahead!")        
    














