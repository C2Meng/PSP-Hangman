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
firekeeper_png = [1,2,3,4,5,6]
firekeeper_png[0]= pygame.image.load("assets/firekeeper1.png") #1
firekeeper_png[1]= pygame.image.load("assets/firekeeper2.png") #2
firekeeper_png[2]= pygame.image.load("assets/firekeeper3.png") #3
firekeeper_png[3]= pygame.image.load("assets/firekeeper4.png") #4
firekeeper_png[4]= pygame.image.load("assets/firekeeper5.png") #5
firekeeper_png[5]= pygame.image.load("assets/firekeeper6.png") #6

#game
firekeeper_status = 0 



#game loop
running = True
while running:
    pygame.display.update()
    screen.blit(firekeeper_png[firekeeper_status],(150,100))
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

