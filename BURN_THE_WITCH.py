# ********************************************************* 
# Program: BURN_THE_WITCH.py 
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Class: TL10
# Year: 2023/24 Trimester 1 
# Names: WINNIE LEE WEN NI | SOFIA BINTI HANISMAN | YAP YANG YI | CHAN CHUAN MENG
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3 | 1221107931
# Emails: @student.mmu.edu.my | @student.mmu.edu.my | @student.mmu.edu.my | 1221107931@student.mmu.edu.my
# Phones: +6 | +6 | +6 | +60125293192
# ********************************************************* 

# ********************************************************* 
# TO DO LIST
# 1. option button for difficulty, categories etc
# 2. user login screen
# 3. leaderboard
# 4. minigame
# 5. intro screen
# 6. game repeat loop (I.E: asking user want play again anot (Y/N))
# -Reset lives, reset word, reset guess









# ********************************************************* 


import pygame,sys
import random
import time

pygame.init()
#screen
FPS = 60
FPS_CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))

#background
background = pygame.image.load("assets/background3.jpg")
background = pygame.transform.scale(background, (1000,600))
pygame.display.set_caption("Burn the Witch!")


#import images 
status_png = [0,1,2,3,4,5,6]
status_png[0] = pygame.image.load("assets/firekeeper1.png")
status_png[1] = pygame.image.load("assets/firekeeper2.png")
status_png[2] = pygame.image.load("assets/firekeeper3.png")
status_png[3] = pygame.image.load("assets/firekeeper4.png")
status_png[4] = pygame.image.load("assets/firekeeper5.png")  #make sure there is the corresponding pngs in the assets folder! PROGRAM WILL NOT RUN IF NO IMAGES WITHT THE SAME NAME.
status_png[5] = pygame.image.load("assets/firekeeper6.png")
status_png[6] = pygame.image.load("assets/firekeeper6.png")

  #these can be made more efficient but no brain power atm
player = pygame.image.load("assets/knight.png")
#if index out of range = game CTD (Crash to desktop)

#game vars
correct_guess =0
correct_guesses = []
wrong_guesses =[]
guessed_alphabet = []
#user input
input_letter = ''

#attempts
firekeeper_status = 0
attempts = 6

#words lists
word = ["applepie","car","pizza","popular", "estus", "bonfire", "souls", "ember", "undead", 
        "lordvessel", "hollow", "kindled", "sunbro", "covenant"]
guessed_word = random.choice(word)
hidden_word = ["_"] * len(guessed_word)

#colour
white = (255,255,255)
black = (0,0,0)

#fonts
font1 = pygame.font.SysFont('times new roman',60)
font2 = pygame.font.SysFont('times new roman',30)
game_text = pygame.font.SysFont('times new roman',40)
menu_text = pygame.font.SysFont('times new roman', 80)
small_text = pygame.font.SysFont('times new roman', 20)

#def leaderboard():
     
#def quit():
def intro():
     
    running = True
    while running:
          screen.fill("black")


          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()


          pygame.display.update()

def try_Again():
     #button for repeat loop
     #ask if player wan play again
     #if yes, repeat, reset all variables,reset to option screen
     #if no quit pygame
     #bug where attempts go into negatives
     #make sure user cannot make any more guess attempts

     print("this is a dummy string")
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
     global attempts
     global firekeeper_status
     global correct_guess
     running = True 
     while running:
          screen.blit(background, (0,0))
          screen.blit(status_png[firekeeper_status],(630,150))
          screen.blit(player, (10,265))
          #word randomiser
          #def randomiser():
               #return random.choice(words)
                
          #word display
          #randomiser()
          

          #text = game_text.render(word_display ,1, 'black')
          #screen.blit(text, ( 400,200))
          

          #displays
          def display_guess_word():
              word_text = font1.render(" ".join(hidden_word), True, white)
              screen.blit(word_text, (150,200))

          def display_invalid_guess():
               invalid_surface = pygame.Surface((400,400))
               screen.blit(invalid_surface, (40.,40))
               invalid_text = font2.render("The current letter is invalid", True , "grey")
               screen.blit(invalid_text,(20,20))

          def display_attempts():
            attempts_surface = pygame.Surface((210,40))
            screen.blit(attempts_surface, (15,15))
            attempts_text = font2.render(f"Attempts left:  {attempts}", True, white)
            screen.blit(attempts_text, (20,20))

          def display_lose():
            win_surface= pygame.Surface((1000,80))
            screen.blit(win_surface, (0,100))
            lose_text = font1.render("YOU LOSE!", True, "red")
            screen.blit(lose_text, (335,105))

          def display_win():
            lose_surface= pygame.Surface((1000,80))
            screen.blit(lose_surface, (0,100))
            lose_text = font1.render("TRIBULATION PASSED", True, "yellow")
            screen.blit(lose_text, (180,105))

          display_guess_word()
          display_attempts()
          
               
            
     
          
          for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            running = False
                            sys.exit()
                        
        
                                        #detect user input
                        if event.type == pygame.KEYDOWN:
                             input_letter = event.unicode.lower()
                             if event.key == pygame.K_BACKSPACE:
                                  input_letter = input_letter [:-1]

                             number = False
                             if input_letter not in guessed_alphabet:
                                  
                                
                                  
                                  guessed_alphabet.append(input_letter)
                                  
                                  # Check if the letter is in the guessed word
                                  
                                  
                                  if input_letter in guessed_word:
                                      for i in range(len (guessed_word)):
                                          if guessed_word[i] == input_letter:
                                              hidden_word[i] = input_letter
                                              correct_guess += 1
                                              
                                              
                                             
                                  elif input_letter not in guessed_word:
                                    attempts -= 1
                                    firekeeper_status += 1

                             else:
                                  break
                                    
        
        

          print(guessed_alphabet)     
          #wincon check      
          won = True
          end = False
          for letter in guessed_word:
               if letter not in guessed_alphabet:
                    won = False
                    break

          if attempts <=0:
                display_lose()
                firekeeper_status = 0
                #make sure no funny business with attempts counter
                if attempts < 0 :
                    attempts +=  +1 
               
                running = False
                attempts = 6
                break
                #Win = True to detect loss con instead of just display_lose, same for win con
                #attempt keyboard lock when in win/loss screen
                #call the try again? function
          if won:
               display_win()
               running = False
               attempts = 6
               break
          
          running = True      
                
               
                  #display_win()
                #call try again function
          
          
          
          pygame.display.update()

def main_menu():

    running = True
    color_loop = True
    while running:
        screen.fill("black")
        #screen.blit(background, (0,0))

        #displaying menu text
        display = "BURN THE WITCH"
        sub_display = "press any key to start"
        text_1 = menu_text.render(display, 1, "white")
        screen.blit(text_1, (150,200))

        text_2 = small_text.render(sub_display, 1, "white")
        screen.blit(text_2, (386,400))
        
        #while color_loop:
             #text_2 = small_text.render(sub_display, 1, "grey")
             #text_2 = small_text.render(sub_display, 1, "white")

    



        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    game()

        pygame.display.update()


main_menu()
pygame.quit()
