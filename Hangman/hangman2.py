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

#word lists
words = ["estus", "bonfire", "souls", "ember", "undead", "lordvessel", "hollow", "kindled", "sunbro", "covenant" ]
word = random.choice(words)
word = str(word).upper()

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
#game vars
correct_guess =[]
wrong_guesses =[]
lives = 6
status = 0





def game():
     running = True 
     while running:
          screen.fill("white")

          #word randomiser
          #def randomiser():
               #return random.choice(words)
                
          #word display
          #randomiser()
          word_display = ""
          
          
          for letter in word:
            
          
            if letter in correct_guess:
                word_display += letter + " "

          
            else:
                word_display += "_" + " "

          text = game_text.render(word_display ,1, 'black')
          screen.blit(text, ( 500,200))

        
               
            
     
          
          for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            running = False
                            sys.exit()
          pygame.display.update()
            

        
#fonts

game_text = pygame.font.SysFont('times new roman',40)
menu_text = pygame.font.SysFont('times new roman', 80)
small_text = pygame.font.SysFont('times new roman', 25)

#def leaderboard():
     
#def quit():


def main_menu():

    running = True
    while running:
        screen.fill("black")
        #screen.blit(background, (0,0))
        #displaying menu text
        display = "BURN THE WITCH"
        sub_display = "press any key to start"
        text_1 = menu_text.render(display, 1, "white")
        screen.blit(text_1, (150,200))

        text_2 = small_text.render(sub_display, 1, "white")
        screen.blit(text_2, (370,400))

    



        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    game()

        pygame.display.update()


main_menu()
