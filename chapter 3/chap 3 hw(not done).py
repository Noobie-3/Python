from lib2to3.pytree import convert
import sys
from xml.dom.pulldom import default_bufsize





#The Convertor/Try again Function

def convertor():  
    scores = input ("Enter your score: ")
    floatScores = float(scores)
    if floatScores >= 0 and floatScores < 60:
        print ("You have a: F")
    elif floatScores >= 60 and floatScores < 66:
        print ("You have a: D")
    elif floatScores >= 67 and floatScores < 79:
        print ("You have a: C")
    elif floatScores >= 80 and floatScores < 87:
        print ("You have a: B")
    elif floatScores >= 88 and floatScores <= 100:
        print ("You have an: A")
#not working as intennded ask teach
        while True:
            inp = input("Wanna Try again: ")
            if inp == "N" or inp == "n":
                break
            elif inp == "Y" or inp == "y":
                convertor()

    
convertor()
