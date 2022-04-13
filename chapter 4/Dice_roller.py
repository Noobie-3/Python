import random 

def dice_roll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total_score = die1 + die2
    print("\nDie Number 1 rolled...",die1)
    print("\nDie Number 2 rolled...", die2)

    if die1 == 1 and die2 == 1:
        print("You got snake eyes what a shame........")
    elif die1 == 6 and die2 == 6:
        print("Hey thats boxcars NICE JOB")
    print("\nThe total of the roll is...",total_score)


  
def repeat():
    answer = input("DO you wanna roll the dies (Accepts the letters Y ot N): ")
    if answer == "Y" or answer == "y":
        dice_roll(),repeat()
    if answer == "N" or answer == "n":
        exit()
    elif answer != "Y" or answer != "y" or answer != "N" or answer != "n":
        print("Wrong Entry please enter N or Y"),repeat()


repeat()

