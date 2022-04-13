import sys
import random




grid = [
        [], [], [],
        [], [], [],
        [], [], []
        ] 

#Usable spaces on board
grid[0] = ' '
grid[1] = ' '
grid[2] = ' '
grid[3] = ' '
grid[4] = ' ' 
grid[5] = ' '
grid[6] = ' '
grid[7] = ' '
grid[8] = ' '
 
#Playing board
def PrintBoard():
    print("+---+---+---+", 
      "\n|", grid[0],  "|", grid[1],   "|",grid[2],   "|",
      "\n+---+---+---+",
      "\n|", grid[3],  "|", grid[4],   "|",grid[5],   "|",
      "\n+---+---+---+",
      "\n|", grid[6],  "|", grid[7],   "|",grid[8],   "|",
      "\n+---+---+---+")

win = False

#logic behind your turn could be simplyfied someho
def xTurn():
    collum = int(input("what collum:"))
    while collum <=0 or collum >= 4:
        collum = int(input("what collum:"))

    row = int(input("what row"))
    while row <=0 or row >= 4:
       row = int(input("What row"))
    
    #Grid 0
    while collum == 1 and row == 1:
        if grid[0] == 'X' or grid[0] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column"))
            row = int(input("What row"))
        elif grid[0] != 'X':
            grid[0] = 'X'
            collum = ' '
            row = ' '
    
    #Grid 3
    while collum == 1 and row == 2:
        if grid[3] == 'X' or grid[3] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[3] != 'X':
            grid[3] = 'X'
            collum = ' '
            row = ' '      
            
    #Grid 6    
    while collum == 1 and row == 3:
        if grid[6] == 'X' or grid[6] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[6] != 'X':
            grid[6] = 'X'
            collum = ' '
            row = ' '    
            
    #Grid 1
    while collum == 2 and row == 1:
        if grid[1] == 'X' or grid[1] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[1] != 'X':
            grid[1] = 'X'
            collum = ' '
            row = ' '     
            
    #Grid 4  
    while collum == 2 and row == 2:
        if grid[4] == 'X' or grid[4] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[4] != 'X':
            grid[4] = 'X'
            collum = ' '
            row = ' '       
            
    #Grid 7    
    while collum == 2 and row == 3:
        if grid[7] == 'X' or grid[7] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[7] != 'X':
            grid[7] = 'X'
            collum = ' '
            row = ' '      
    
    #Grid 2
    while collum == 3 and row == 1:
        if grid[2] == 'X' or grid[2] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[2] != 'X':
            grid[2] = 'X'
            collum = ' '
            row = ' '       
    
    #Grid 5    
    while collum == 3 and row == 2:
        if grid[5] == 'X' or grid[5] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[5] != 'X':
            grid[5] = 'X'
            collum = ' '
            row = ' '
    
    #Grid 8   
    while collum == 3 and row == 3:
        if grid[8] == 'X' or grid[8] == 'O':
            print("Can not choose this spot ", collum, row)
            collum = int(input("What column: "))
            row = int(input("What row: "))
        elif grid[8] != 'X':
            grid[8] = 'X'
            collum = ' '
            row = ' '      
    return grid

#computer turn
def Oturn():
    random_Index = random.randint(0,len(grid)-1)
    print(grid[random_Index])

    while grid[random_Index] == 'X' or grid[random_Index] == 'O':
        random_Index = random.randint(0,len(grid)-1)
        print(grid[random_Index])
    if grid[random_Index] != 'X' or grid[random_Index] != 'O':
        grid[random_Index] = 'O'
        PrintBoard()
               
#check if you won        
def win_end_game():
    PrintBoard()

    sys.exit()
def lose_end_game():
    PrintBoard()
    print("YOU Lost!!!!")
    sys.exit()
   
#main funcion     
def game():
    PrintBoard()
    win = False
    while win ==False: 
        xTurn()
        checkWin()
        Oturn()
        checkWin()

def checkWin():

    #horizonal check win
    if grid[0] == 'X' and grid[1] == 'X' and grid[2] == 'X':
        win_end_game()
    elif grid[3] == 'X' and grid[4] == 'X' and grid[5] == 'X':
        win_end_game()
    elif grid[6] == 'X' and grid[7] == 'X' and grid[8] == 'X':
        win_end_game()

    #horszinal lose check
    if grid[0] == 'O' and grid[1] == 'O' and grid[2] == 'O':
        lose_end_game()
    elif grid[3] == 'O' and grid[4] == 'O' and grid[5] == 'O':
        lose_end_game()
    elif grid[6] == 'O' and grid[7] == 'O' and grid[8] == 'O':
        lose_end_game()

    #vertical check
    if grid[0] == 'X' and grid[3] == 'X' and grid[6] == 'X':
        win_end_game()
    elif grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X':
        win_end_game()
    elif grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X':
        win_end_game()  

    #vertical lose check
    if grid[0] == 'O' and grid[3] == 'O' and grid[6] == 'O':
        lose_end_game()
    elif grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O':
        lose_end_game()
    elif grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O':
        lose_end_game()

    #cross win check
    if grid[0] == 'X' and grid[4] == 'X' and grid[8] == 'X':
        win_end_game()
    elif grid[6] == 'X' and grid[4] == 'X' and grid[2] == 'X':
        win_end_game()
    #cross lose check
    if grid[0] == 'O' and grid[4] == 'O' and grid[8] == 'O':
        lose_end_game()
    elif grid[6] == 'O' and grid[4] == 'O' and grid[2] == 'O':
        lose_end_game()
        


game()