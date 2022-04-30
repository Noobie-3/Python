# AdCap Ripoff

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
                
                
                
    screen.fill(background)
    task1, red_length, draw_red = draw_task(red, 50, red_value, draw_red, red_length, red_speed)
    task2, orange_length, draw_orange = draw_task(orange, 110, orange_value, draw_orange, orange_length, orange_speed)
    task3, yellow_length, draw_yellow = draw_task(yellow, 170, yellow_value, draw_yellow, yellow_length, yellow_speed)
    task4, green_length, draw_green = draw_task(green, 230, green_value, draw_green, green_length, green_speed)
    task5, blue_length, draw_blue = draw_task(blue, 290, blue_value, draw_blue, blue_length, blue_speed)
    task6, purple_length, draw_purple = draw_task(purple, 350, purple_value, draw_purple, purple_length, purple_speed)
    
    display_score = font.render('Money: $'+str(round(score,2)),True, white, black)
    screen.blit(display_score, (10, 5))
    
    pygame.display.flip()

pygame.quit
            
            
    
    

