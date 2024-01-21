# ********************************************************* 
# Program: BURN_THE_WITCH.py 
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Class: TL10-01
# Year: 2023/24 Trimester 1 
# Names: WINNIE LEE WEN NI | YAP YANG YI | SOFIA BINTI HANISMAN| CHAN CHUAN MENG
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3 | 1221107931
# Emails: @student.mmu.edu.my | @student.mmu.edu.my | @student.mmu.edu.my | 1221107931@student.mmu.edu.my
# Phones: +6 | +6 | +6 | +60125293192
# ********************************************************* 

# ********************************************************* 
# TO DO LIST
# 1. option button for difficulty 
# 2. user login screen
# 3. leaderboard
# 4. minigame
# 5. intro screen
# 6. game repeat loop (I.E: asking user want play again anot (Y/N))
# ********************************************************* 

import pygame,sys
import random


pygame.init()
#screen
FPS = 60
screen = pygame.display.set_mode((1000,600))

#background
background = pygame.image.load("assets/background3.jpg")
background = pygame.transform.scale(background, (1000,600))
pygame.display.set_caption("Burn the Witch!")

#import images 
status_png = [0,1,2,3,4,5]
status_png[0] = pygame.image.load("assets/firekeeper1.png")
status_png[1] = pygame.image.load("assets/firekeeper2.png")
status_png[2] = pygame.image.load("assets/firekeeper3.png")
status_png[3] = pygame.image.load("assets/firekeeper4.png")
status_png[4] = pygame.image.load("assets/firekeeper5.png") 
status_png[5] = pygame.image.load("assets/firekeeper6.png") 
player = pygame.image.load("assets/knight.png")


#game vars
win_con = False
correct_guess =0
wrong_guesses =[]##-------
firekeeper_status = 0
attempts = 5

#user input
input_letter = ''

#words lists
word = ["applepie","car","pizza","popular", "estus", "bonfire", "souls", "ember", "undead", 
        "lordvessel", "hollow", "kindled", "sunbro", "covenant"]
guessed_word = random.choice(word)
hidden_word = ["_"] * len(guessed_word)

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
     global win_con
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
          def display_wrong_guesses(): ##-------S
               wrong_guesses_text = font2.render(" ".join(wrong_guesses), True, "white")
               screen.blit(wrong_guesses_text, (150, 230))
               
          def display_guess_word():
              word_text = font1.render(" ".join(hidden_word), True, "white")
              screen.blit(word_text, (150,150))

          def display_attempts():
            attempts_surface = pygame.Surface((210,40))
            screen.blit(attempts_surface, (15,15))
            attempts_text = font2.render(f"Attempts left:  {attempts}", True, "white")
            screen.blit(attempts_text, (20,20))

          def display_lose():
            win_surface= pygame.Surface((1000,80))
            screen.blit(win_surface, (0,100))
            lose_text = font1.render("YOU LOST", True, "red")
            screen.blit(lose_text, (335,105))

          def display_win():
            lose_surface= pygame.Surface((1000,80))
            screen.blit(lose_surface, (0,100))
            lose_text = font1.render("YOU WIN", True, "yellow")
            screen.blit(lose_text, (330,105))

          display_guess_word()
          display_attempts()
          display_wrong_guesses() ##-------S
          
               
            
     
          
          for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            running = False
                            sys.exit()
                        
                        if win_con == False:   
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    input_letter = input_letter [:-1]
                                else:
                                    input_letter = event.unicode.lower()

                                    # Check if the letter is in the guessed word
                                    if input_letter in guessed_word:
                                        for i in range(len(guessed_word)):
                                            if guessed_word[i] == input_letter:
                                                hidden_word[i] = input_letter
                                                    
                                    elif input_letter not in guessed_word and input_letter not in wrong_guesses: ##-------S
                                        wrong_guesses.append(input_letter)
                                        attempts -= 1
                                        firekeeper_status += 1
                               
          if attempts <= 0:
                display_lose()
                firekeeper_status = 0 
                if attempts < 0 :
                    attempts +=  +1 
                win_con = True

          elif "_" not in hidden_word: ##-------S
                display_win()
                win_con = True
          
          
          
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
    

        
    
    
    
