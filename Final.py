# AdCap Ripoff

from multiprocessing import Manager
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
screen = pygame.display.set_mode([400, 500])
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
score = 0
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

def draw_button(color, xCord, cost, owned, managerCost):
    color_button = pygame.draw.rect(screen, color, [xCord, 385, 55, 50])
    color_cost = font.render(str(round(cost, 1)), True, black)
    screen.blit(color_cost, (xCord + 6, 390))
    if not owned:
        managerButton = pygame.draw.rect(screen, color, [xCord, 440, 55, 30])
        managerText = color_cost = font.render(str(round(managerCost, 2)), True, black)
        screen.blit(managerText, (xCord + 1, 440))
    return color_button, managerButton
    
    
    
#if game is running do this
running = True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_red = True
            if task2.collidepoint(event.pos):
                draw_orange = True
            if task3.collidepoint(event.pos):
                draw_yellow = True
            if task4.collidepoint(event.pos):
                draw_green = True
            if task5.collidepoint(event.pos):
                draw_blue = True
            if task6.collidepoint(event.pos):
                draw_purple = True                
                
                
    # makes the play area populated with task to do
    screen.fill(background)
    
    #red task
    task1, red_length, draw_red = draw_task(red, 50, red_value, draw_red, red_length, red_speed)
    redBuy, redManagerBuy = draw_button(red, 10, redCost, redOwned, redManagerCost)
    
     #orange task
    task2, orange_length, draw_orange = draw_task(orange, 110, orange_value, draw_orange, orange_length, orange_speed)
    orangeBuy, redManagerBuy = draw_button(orange, 70, orangeCost, orangeOwned, orangeManagerCost)
    
    #yellow task
    task3, yellow_length, draw_yellow = draw_task(yellow, 170, yellow_value, draw_yellow, yellow_length, yellow_speed)
    yellowBuy, yellowyellowManagerBuy = draw_button(yellow, 130, yellowCost, yellowOwned, yellowManagerCost)
    
    #green task
    task4, green_length, draw_green = draw_task(green, 230, green_value, draw_green, green_length, green_speed)
    greenBuy, greenManagerBuy = draw_button(green, 190, greenCost, greenOwned, greenManagerCost)
    
    #blue task
    task5, blue_length, draw_blue = draw_task(blue, 290, blue_value, draw_blue, blue_length, blue_speed)
    blueBuy, blueManagerBuy = draw_button(blue, 250, blueCost, blueOwned, blueManagerCost)
    
    #purple task
    task6, purple_length, draw_purple = draw_task(purple, 350, purple_value, draw_purple, purple_length, purple_speed)
    purpleBuy, purpleManagerBuy = draw_button(purple, 310, purpleCost, purpleOwned, purpleManagerCost)


 

 
    
    display_score = font.render('Money: $'+str(round(score,2)),True, white, black)
    screen.blit(display_score, (10, 5))
    
    pygame.display.flip()

pygame.quit
            
            
    
    

