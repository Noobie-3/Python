# ROCK - PAPER - SCISSORS

import random
import time
import string

rock = 1
paper = 2 
sissors = 3



#User Input
def play_game():
    random.seed(time.time())
    houseChoice = random.randint(1, 3)
    print("\nRULES FOR THE GAME\nRock beats paper\nPaper beats Rock\nSissors Beats Paper\n=======================")
    userChoice = input("Please enter a Rock, Paper, or Sissors: ")

    while userChoice.isdigit():
        print("User input must be Rock, Paper, or Sissors.")
        userChoice = input("Please enter Rock, Paper, or Sissors: ")

#Changes "word" to num
    if userChoice.lower() == "rock":
        userChoice = 1
        
    elif userChoice.lower() == "paper":
        userChoice = 2

    elif   userChoice.lower() == "sissors":
        userChoice = 3
    
    while userChoice < 1 or userChoice > 3:
        print("Number entered must be between 1 and 3.")
        userChoice = input("Please enter a number between 1 and 3: ")

#ROCK CHOICES
    if userChoice == rock and houseChoice == paper :
        print("\nYou lost: Paper covers Rock! \n")
    elif userChoice == rock and houseChoice == rock:
        print("\nYou Tied: Rock cannot beat Rock!\n")
    elif userChoice == rock and houseChoice == sissors:
        print("\nYou win: Rock decimates Sissors!\n")
#PAPER CHOICES
    elif userChoice == paper and houseChoice == sissors:
        print("\nYou Lost: Sissors Cuts paper!\n")
    elif userChoice == paper and houseChoice == paper:
        print("\nYou Tied: Paper Can not fold Paper!\n")
    elif userChoice == paper and houseChoice == rock:
        print("\nYou Win: Paper Covers Rocks eyes so it can not see!\n")
#SISSORS CHOICES
    elif userChoice == sissors and houseChoice == rock:
        print("\nYou Lost: Sissors blades are now dull from fighting Rock!\n")
    elif userChoice == sissors and houseChoice == sissors:
        print("\nYou tied: Sissors found its match and decided not to fight!\n")
    elif userChoice == sissors and houseChoice == paper:
        print("\nYou win: Sissors choped paper into tiny pieces!\n")
    
def main():
    play_game()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()