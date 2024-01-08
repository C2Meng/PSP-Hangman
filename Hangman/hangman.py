import pygame, sys
import random
from list import easy_categories_list

pygame.init()


#create screen
Background=pygame.image.load("assets/BG.png")
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption ("Hangman")


#game loop
running = True
while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    pygame.display.update()
