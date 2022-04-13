import pygame
 
win = pygame.display.set_mode((500,600))
pygame.display.set_caption("Seziuse garanteed")

x = 50
y = 50
width = 40
height = 60
vel = 55

 
def flash():
    win.fill((0, 150, 255))  # Fills the screen with black  
    pygame.display.update() 

    win.fill((255,0,0))  # Fills the screen with black 
    pygame.display.update() 

yes = 1
while yes == 1: 
    flash()

