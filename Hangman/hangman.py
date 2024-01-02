import pygame
import os

import random


#terminal where game happens
screen = pygame.display.set_mode((800,600))



#making the bg stick until the user quits
Running = True
while Running:

    screen.fill((0,0,0))
    screen.blit(screen, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.quit():
            Running = False


pygame.quit()
