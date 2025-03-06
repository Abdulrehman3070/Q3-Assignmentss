Greet = "Welcome to my computer quiz!"
score = 0
playing = input(f"""{Greet}
Do you want to Play Quiz? = """)

if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's Play:) ")

question = str(input("What Does CPU Stand for? = "))

if question.lower() == "central processing unit":
    print("Congrats, Correct Answer:)")
    score+=1
else:
    print("Wrong Answer") 

question = str(input("What Does GPU Stand for? = "))

if question.lower() == "graphical processing unit":
    print("Congrats, Correct Answer:)")
    score+=1
else:
    print("Wrong Answer")

question = str(input("What Does RAM Stand for? = "))

if question.lower() == "random access memory":
    print("Congrats, Correct Answer:)")
    score+=1
else:
    print("Wrong Answer")

question = str(input("What Does ROM Stand for? = "))

if question.lower() == "read only memory":
    print("Congrats, Correct Answer:)")
    score+=1
else:
    print("Wrong Answer")
    quit()

print(f"Your got {score} questions correct!")
