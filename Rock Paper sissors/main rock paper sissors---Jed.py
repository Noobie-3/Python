# ROCK - PAPER - SCISSORS

import random
import time


rock = 1
paper = 2 
sissors = 3

def play_game():
    random.seed(time.time())
    houseChoice = random.randint(1, 3)
    
    userChoice = input("Please enter a number between 1 and 3: ")

    while not userChoice.isdigit():
        print("User input must be a number between 1 and 3.")
        userChoice = input("Please enter a number between 1 and 3: ")

    userChoice = int(userChoice)

    while userChoice < 1 or userChoice > 3:
        print("Number entered must be between 1 and 3.")
        userChoice = int(input("Please enter a number between 1 and 3: "))

#ROCK CHOICES
    if userChoice == rock and houseChoice == paper :
        print("You lost: Paper covers Rock! ")
    elif userChoice == rock and houseChoice == rock:
        print("You Tied: Rock cannot beat Rock!")
    elif userChoice == rock and houseChoice == sissors:
        print("You win: Rock decimates Sissors!")

#PAPER CHOICES
    elif userChoice == paper and houseChoice == sissors:
        print("You Lost: Sissors Cuts paper!")
    elif userChoice == paper and houseChoice == paper:
        print("You Tied: Paper Can not fold Paper!")
    elif userChoice == paper and houseChoice == rock:
        print("You Win: Paper Covers Rocks eyes so it can not see!")

#SISSORS CHOICES3

    elif userChoice == sissors and houseChoice == rock:
        print("You Lost: Sissors blades are now dull from fighting Rock!")
    elif userChoice == sissors and houseChoice == sissors:
        print("You tied: Sissors found its match and decided not to fight!")
    elif userChoice == sissors and houseChoice == paper:
        print("You win: Sissors choped paper into tiny pieces!")
    
def main():
    play_game()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()