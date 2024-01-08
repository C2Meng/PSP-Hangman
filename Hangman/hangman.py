import pygame, sys
import random
from list import easy_categories_list

pygame.init()
FPS = 60
clock = pygame.time.Clock()

#create screen
Background=pygame.image.load("assets/BG.png")
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption ("Hangman")

#Status progression// images 
status_png = [0,1,2,3,4,5]
status_png[0] = pygame.image.load("assets/firekeeper1.png")
status_png[1] = pygame.image.load("assets/firekeeper2.png")
status_png[2] = pygame.image.load("assets/firekeeper3.png")
status_png[3] = pygame.image.load("assets/firekeeper4.png")
status_png[4] = pygame.image.load("assets/firekeeper5.png")  #make sure there is the corresponding pngs in the assets folder 
status_png[5] = pygame.image.load("assets/firekeeper6.png")  #these can be made more efficient but no brain power atm


#game
firekeeper_status = 3



#game loop
running = True
while running:
    pygame.display.update()
    screen.blit(status_png[firekeeper_status],(150,100))
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


