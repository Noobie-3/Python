# AdCap Ripoff

from multiprocessing import Manager
from turtle import ycor
import pygame
pygame.init()


#color library
red = (255, 0, 0)
green = (0, 255,0)
blue = (0,0,255)
white = (255, 255, 255)
black = (0,0,0)
purple = (175,0,255)
orange = (255,165,0)
yellow = (255,255,0)

#variables
screen = pygame.display.set_mode([430, 600])
pygame.display.set_caption("Toltally not a ripoff of a popular idle game")
background = black
framerate = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
draw_red = False
draw_orange = False
draw_yellow = False
draw_green = False
draw_blue = False
draw_purple = False
red_length = 0
orange_length = 0
yellow_length = 0
green_length = 0
blue_length = 0
purple_length = 0
red_speed = 6
orange_speed = 5
yellow_speed = 4
green_speed = 3
blue_speed = 2
purple_speed = 1
score = 10000000000
#draw buttons 
#red buttons
redCost = 1
redOwned = False
redManagerCost = 100
#orange button
orangeCost = 2
orangeOwned = False
orangeManagerCost = 500
#yellow button
yellowCost = 3
yellowOwned = False
yellowManagerCost = 1900
#green button
greenCost = 4
greenOwned = False
greenManagerCost = 4000
#blue button
blueCost = 5
blueOwned = False
blueManagerCost = 10000
#purple button
purpleCost = 6
purpleOwned = False
purpleManagerCost = 100000





#game variables
red_value = 1
orange_value = 2
yellow_value = 3
green_value = 4
blue_value = 5
purple_value = 6

def draw_task(color, yCord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False 
        length = 0
        score += value 
    task = pygame.draw.circle(screen, color, (30, yCord ), 20, 5)
    pygame.draw.rect(screen, color, [70, yCord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75,yCord - 10, 190, 20])
    pygame.draw.rect(screen, color, [70,yCord - 15, length,30])
    value_text = font.render(str(value), True, white)
    screen.blit(value_text, (16, yCord - 10))
    return task, length, draw

def draw_button(color, xCord,yCord, cost, owned, managerCost):
    color_button = pygame.draw.rect(screen, color, [xCord, yCord, 60, 40])
    color_cost = font.render(str(round(cost, 1)), True, black)
    screen.blit(color_cost, (xCord + 1, yCord))
    yCord = yCord + 80
    if not owned:
        managerButton = pygame.draw.rect(screen, color, [xCord, yCord, 60, 40])
        managerText = color_cost = font.render(str(round(managerCost, 2)), True, black)
        screen.blit(managerText, (xCord + 1, yCord))
    else:
        managerButton = pygame.draw.rect(screen, black, [xCord, yCord, 60, 40])
    return color_button, managerButton
    
    
    
#if game is running do this
running = True
while running:
    timer.tick(framerate)
    #if manager is owner auto get moneys
    if redOwned and not draw_red:
        draw_red = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #Red button dection
            if task1.collidepoint(event.pos):
                draw_red = True
            if redManagerBuy.collidepoint(event.pos) and score >= redManagerCost and not redOwned:
                redOwned = True
                score -= redManagerCost
                
            #Orange button detection
            if task2.collidepoint(event.pos):
                draw_orange = True
            if orangeManagerBuy.collidepoint(event.pos) and score >= orangeManagerCost and not orangeOwned:
                orangeOwned = True
                score -= orangeManagerCost                
            #yellow button detection
            if task3.collidepoint(event.pos):
                draw_yellow = True
            if yellowManagerBuy.collidepoint(event.pos) and score >= yellowManagerCost and not yellowOwned:
                yellowOwned = True
                score -= yellowManagerCost    
                
            #green button detection
            if task4.collidepoint(event.pos):
                draw_green = True
            if greenManagerBuy.collidepoint(event.pos) and score >= greenManagerCost and not greenOwned:
                greenOwned = True
                score -= greenManagerCost
                
            #blue button detection
            if task5.collidepoint(event.pos):
                draw_blue = True
            if blueManagerBuy.collidepoint(event.pos) and score >= blueManagerCost and not blueOwned:
                blueOwned = True
                score -= blueManagerCost  
                
            #purple button detectection
            if task6.collidepoint(event.pos):
                draw_purple = True                
            if purpleManagerBuy.collidepoint(event.pos) and score >= purpleManagerCost and not purpleOwned:
                purpleOwned = True
                score -= purpleManagerCost

                
                
                
    # makes the play area populated with task to do
    screen.fill(background)
    
    #red task
    task1, red_length, draw_red = draw_task(red, 50, red_value, draw_red, red_length, red_speed)
    redBuy, redManagerBuy = draw_button(red, 10, 410, redCost, redOwned, redManagerCost)
    
     #orange task
    task2, orange_length, draw_orange = draw_task(orange, 110, orange_value, draw_orange, orange_length, orange_speed)
    orangeBuy, orangeManagerBuy = draw_button(orange, 80, 410, orangeCost, orangeOwned, orangeManagerCost)
    
    #yellow task
    task3, yellow_length, draw_yellow = draw_task(yellow, 170, yellow_value, draw_yellow, yellow_length, yellow_speed)
    yellowBuy, yellowManagerBuy = draw_button(yellow, 150, 410, yellowCost, yellowOwned, yellowManagerCost)
    
    #green task
    task4, green_length, draw_green = draw_task(green, 230, green_value, draw_green, green_length, green_speed)
    greenBuy, greenManagerBuy = draw_button(green, 220, 410, greenCost, greenOwned, greenManagerCost)
    
    #blue task
    task5, blue_length, draw_blue = draw_task(blue, 290, blue_value, draw_blue, blue_length, blue_speed)
    blueBuy, blueManagerBuy = draw_button(blue, 290, 410, blueCost, blueOwned, blueManagerCost)
    
    #purple task
    task6, purple_length, draw_purple = draw_task(purple, 350, purple_value, draw_purple, purple_length, purple_speed)
    purpleBuy, purpleManagerBuy= draw_button(purple, 360, 410, purpleCost, purpleOwned, purpleManagerCost)

 

 
    
    display_score = font.render('Money: $'+str(round(score,2)),True, white, black)
    screen.blit(display_score, (10, 5))
    
    #writes buy more?
    buyMore = font.render("Buy More", True, white)
    screen.blit(buyMore, (10, 385) )
    #writes buy managers
    buyManagers = font.render("Buy Managers", True, white)
    screen.blit(buyManagers, (10, 465) )
    
    
    pygame.display.flip()

pygame.quit
            
            
    
    

