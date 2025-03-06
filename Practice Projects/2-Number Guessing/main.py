import random
score = 0
Greet = "Welcome to my computer quiz!"
playing = input(f"""{Greet}
DO you Want to play Number Guessing Game?(yes/no) = """)
condition = True


random_number = random.randrange(1,11)
if playing.lower() =="yes":    
    while condition:
        score +=1 
        guess = int(input("Make a Guess: "))
        if  guess == random_number :
            
            print(f"Correct, You complete it in your {score} attempt")
            condition = False
        else:
            print("Wrong Guess, Tries Over")
else:
    print("Okay,Have a nice day Ahead")