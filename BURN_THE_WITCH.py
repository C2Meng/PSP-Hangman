# ********************************************************* 
# Program: BURN_THE_WITCH.py 
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Class: TL10-01
# Year: 2023/24 Trimester 1 
# Names: WINNIE LEE WEN NI | YAP YANG YI | SOFIA BINTI HANISMAN| CHAN CHUAN MENG
# IDs: 1221109102 | 1221107539 | 1221107970 | 1221107931
# Emails: 1221109102@student.mmu.edu.my | 1221107539@student.mmu.edu.my | 1221107970@student.mmu.edu.my | 1221107931@student.mmu.edu.my
# Phones: +60 18-258 1460 | +60 14-716 7690 | +60 16-903 5825 | +60 12-529 3192
# ********************************************************* 

# ********************************************************* 
# TO DO LIST
# 1. option button for difficulty 
# 2. user login screen
# 3. leaderboard
# 4. minigame
# 5. intro screen
# 6. game repeat loop (I.E: asking user want play again anot (Y/N)) done
# ********************************************************* 

import pygame,sys
import random
from list_of_words import categories_lists, categories_dict

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

#level difficulty
level = 0

#game vars
win_con = False
correct_guess =0
wrong_guesses =[]
firekeeper_status = 0
attempts = 5
win = False
lose = False

#user input
input_letter = ''

#fonts
font1 = pygame.font.SysFont('times new roman',60)
font2 = pygame.font.SysFont('times new roman',30)
game_text = pygame.font.SysFont('times new roman',40)
menu_text = pygame.font.SysFont('times new roman', 80)
small_text = pygame.font.SysFont('times new roman', 20)
dialogue_text = pygame.font.SysFont('times new roman', 30)

#blit texts shortcut
def blit_text(text, position):
     text = font2.render(text, True, "white")
     screen.blit(text, position)


#categories to choose from
def category(level_categories):
    global result
    global input_choice
    input_choice = ''

    def input_choice_display():
        input_choice_text = font2.render(input_choice, True, "green")
        input_rect = pygame.Rect(375,150,200,50)
        pygame.draw.rect(screen, "white", input_rect,2)
        screen.blit(input_choice_text, (input_rect.x + 5, input_rect.y + 5 ))
    
    def blit_categories_dict(categories):
            blit_text("Type a category, hit enter: ", (325,100))
            y_position = 225
            for i in categories_dict[categories]:
                blit_text(i,(425, y_position) )
                y_position += 50
    

    
    
    running = True
    while running:
          screen.fill("black")
          blit_categories_dict(level_categories)
          input_choice_display()
          
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                          result = input_choice
                          if result in categories_dict[level_categories]:
                                game()
                          else:
                                main_menu()
                        if event.key == pygame.K_BACKSPACE:
                          input_choice = input_choice[:-1]
                        else:
                          input_choice += event.unicode.lower()
                            
                        
                        
                        
            
                         
                     

    
          
          pygame.display.update()

#word generator
def word_gen():
    global hidden_word 
    global guessed_word
    global category_title
    

    word = categories_lists[result] #result is chosen category
    guessed_word = random.choice(word) #randomiser
    category_title = result #title of chosen category
    hidden_word = ["_"] * len(guessed_word)  
    
#reset the game
def reset():
     global win_con
     global correct_guess
     global wrong_guesses
     global attempts
     global firekeeper_status
     
     
     win_con = False
     word_gen()
     wrong_guesses.clear()
     correct_guess = 0
     attempts = 5
     firekeeper_status = 0   

#def leaderboard():
def win_screen():
     #this part resets the game values 
   
     global win
     global lose

     running = True
     while running:
          screen.fill("black")

          def display_win():
            #win_surface= pygame.Surface((1000,80))
            #screen.blit(win_surface, (0,100))
            win_text = menu_text.render("YOU WIN", True, "yellow")
            screen.blit(win_text, (300,200))
            subtext = small_text.render("Press enter to continue", True , "white")
            screen.blit(subtext, (375,300))
          #resetting game vars
          reset()
          win = False
          lose = False
          display_win()
          
        
          
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()
                    
                    if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    if level == 1:
                                        category("intermediate_categories")
                                    if level == 2:
                                        category("difficult_categories")

                                elif event.key == pygame.K_ESCAPE:
                                     pygame.quit()
                                     running = False
                                     sys.exit()
                                     
                    

          pygame.display.update()

def lose_screen():
     global win
     global lose
     
     
     running = True
     while running:
          screen.fill("black")

          #text displays
          def display_lose():
            #lose_surface= pygame.Surface((1000,80))
            #screen.blit(lose_surface, (0,100))
            lose_text = menu_text.render("YOU LOST", True, "red")
            screen.blit(lose_text, (300,200))

            subtext = small_text.render("With this character's death, the thread of prophecy has been severed.", True , "red")
            subtext2 = small_text.render("Restore the game to restore the weave of fate, or persist in the doomed world you have created.", True, "red")
            screen.blit(subtext,(220,300))
            screen.blit(subtext2,(115,320))
            


          reset()
          lose = False
          win = False
          display_lose()  
          
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()

                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.time.delay(200)
                        main_menu()

            
          
          pygame.display.update()
     
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

          name_ask = "Give us your name"
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()
          

          pygame.display.update()

def game():
     #bandaid solution
     global attempts
     global firekeeper_status
     global guessed_word
     global hidden_word
     global correct_guess
     global wrong_guesses
     global win_con
     global win
     global lose
     global level
     

     
     word_gen()
     running = True 
     while running:
          screen.blit(background, (0,0))
          screen.blit(status_png[firekeeper_status],(630,150))
          screen.blit(player, (10,265))
          

          #displays
          def display_wrong_guesses():
              wrong_guesses_text = font2.render(f"wrong guesses: { ',' .join(wrong_guesses)}", True, "white")
              screen.blit(wrong_guesses_text, (150, 230))

          def display_guess_word():
              word_text = font1.render(" ".join(hidden_word), True, "white")
              screen.blit(word_text, (150,150))

          def display_attempts():
            attempts_surface = pygame.Surface((280,65))
            screen.blit(attempts_surface, (15,15))
            alphabet_only_text = small_text.render("Start guessing to save the witch", True, "grey")
            screen.blit(alphabet_only_text, (20, 55))
            attempts_text = font2.render(f"Attempts left:  {attempts}", True, "white")
            screen.blit(attempts_text, (20,20))

          def display_lose():
            win_surface= pygame.Surface((1000,300))
            screen.blit(win_surface, (0,400))
            pygame.time.delay(500)
            char_text = font2.render("Firekeeper", True, "grey")
            screen.blit(char_text, (50,420))
            win_text = dialogue_text.render('"AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"',True, "red")
            screen.blit(win_text, (50,450))

          def display_win():
            win_surface= pygame.Surface((1000,300))
            screen.blit(win_surface, (0,400))
            pygame.time.delay(500)
            char_text = font2.render("Firekeeper", True, "grey")
            screen.blit(char_text, (50,420))
            win_text = dialogue_text.render('"Thank you for saving me, you are now my best friend :)."', True, "green")
            screen.blit(win_text, (50,450))
          
          def display_category():
            category_text = font2.render(category_title, True, "white")
            screen.blit(category_text, (800,10))
          
          display_guess_word()
          display_attempts()
          display_wrong_guesses() 
          display_category()
               
            
     
          
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
                                if input_letter.isalpha():
                                   if input_letter in guessed_word:
                                        for i in range(len(guessed_word)):
                                             if guessed_word[i] == input_letter:
                                                  hidden_word[i] = input_letter        
                                                  
                                   elif input_letter not in guessed_word and input_letter not in wrong_guesses:
                                        wrong_guesses.append(input_letter)
                                        attempts -= 1
                                        firekeeper_status += 1
          #to display levels
          if level == 0:
               blit_text("level 1 : easy", (400, 10))
          if level == 1:
               blit_text("level 2 : intermediate", (400, 10))
          if level == 2:
               blit_text("level 3 : difficult", (400, 10))
            
          #win/lose condition     
          if attempts <= 0:
                display_lose()
                win_con = True
                lose = True

          elif "_" not in hidden_word: 
                display_win()
                win_con = True
                win = True
                level += 1
                

          
          pygame.display.update()
          #if to prevent the following function from immedietly triggering
          if win == True:
             pygame.time.wait(2000)
             win_screen()
             

          elif lose == True:
               pygame.time.wait(2000)
               lose_screen()   
               

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
                    pygame.time.delay(200)
                    category("easy_categories")

        pygame.display.update()



main_menu()
pygame.quit()

        
    
    
    
    
        
    
    
    
