import pygame, sys
import random
from list import easy_categories_list #revision to be made on lists to import

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
status_png[4] = pygame.image.load("assets/firekeeper5.png")  #make sure there is the corresponding pngs in the assets folder! PROGRAM WILL NOT RUN IF NO IMAGES WITHT THE SAME NAME.
status_png[5] = pygame.image.load("assets/firekeeper6.png")  #these can be made more efficient but no brain power atm


#game
firekeeper_status = 0

#guess, "1= fail , 0 = success"
#tobeguessed= "word from list" + len(word) as underline"
#if alphabet in word:
    #alphabet typed will fill in blank underline
    

#suggestion for letter and words (sofia)
#can use if event.key == pygame.K_("Here is where you put the alphabet") to detect keyboard input
#(tedious if you use the if statement for each alphabet, a shortcut if able // maybe functions?? idk)
#how the blank word should appear 

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


