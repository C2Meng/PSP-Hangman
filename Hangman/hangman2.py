import pygame,sys
import random
from souls_like_list import words

pygame.init()
#screen
screen = pygame.display.set_mode((1000,600))

#background
background = pygame.image.load("assets/background3.jpg")
pygame.display.set_caption("Burn the Witch!")

#import images 
status_png = [0,1,2,3,4,5]
status_png[0] = pygame.image.load("assets/firekeeper.jpg")
status_png[1] = pygame.image.load("assets/firekeeper2.png")
status_png[2] = pygame.image.load("assets/firekeeper3.png")
status_png[3] = pygame.image.load("assets/firekeeper4.png")
status_png[4] = pygame.image.load("assets/firekeeper5.png")  #make sure there is the corresponding pngs in the assets folder! PROGRAM WILL NOT RUN IF NO IMAGES WITHT THE SAME NAME.
status_png[5] = pygame.image.load("assets/firekeeper6.png")  #these can be made more efficient but no brain power atm
#player = pygame.image.load("assets/charac.png")

def user_login():
     running = True
     while running:
          screen.fill("black")


          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()


          pygame.display.update()
    

                

def game():
     running = True 
     while running:
          screen.fill("white")
         
          return random.choice(words)
     
     for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()
     pygame.display.update()
            

        

          

#def leaderboard():
     
#def quit():


def main_menu():

    running = True
    while running:

        screen.blit(background, (0,0))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    game()

        pygame.display.update()


main_menu()