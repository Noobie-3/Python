grid = [
        [], [], [],
        [], [], [],
        [], [], []
        ]


grid[0] = 'TTT'
grid[1] = 'O'
grid[2] = 'TGT '
grid[3] = 'O'
grid[4] = 'Test'
grid[5] = 'O '
grid[6] = 'Test1 '
grid[7] = 'O '
grid[8] = 'DSAD '
 

def PrintBoard():
    print("+---+---+---+", 
      "\n|", grid[0],  "|", grid[1],   "|",grid[2],   "|",
      "\n+---+---+---+",
      "\n|", grid[3],  "|", grid[4],   "|",grid[5],   "|",
      "\n+---+---+---+",
      "\n|", grid[6],  "|", grid[7],   "|",grid[8],   "|",
      "\n+---+---+---+")

def game():

    collum = int(input("what collum"))
    while collum <=0 or collum >= 4:
        collum = input("What column")

    row = int(input("what row"))
    while row <=0 or row >= 4:
       row = input("What row")
    
    
    
    if collum == 1 and row == 1:
        print(grid[0])
        
    elif collum == 1 and row == 2:
        print(grid[3])
        
    elif collum == 1 and row == 3:
        print(grid[6])
        
    elif collum == 2 and row == 1:
        print(grid[3])
        
    elif collum == 1 and row == 2:
        print(grid[3])
        
    elif collum == 1 and row == 3:
        print(grid[3])
        
    elif collum == 1 and row == 1:
        print(grid[3])
        
    elif collum == 1 and row == 2:
        print(grid[3])
        
    elif collum == 1 and row == 3:
        print(grid[3])
game()
    
    
    