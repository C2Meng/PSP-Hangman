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
from list_of_words import choose_category, name_category

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
counter = 0
#user input
input_letter = ''
input_choice = ''

#words lists

def category():
    global result
    running = True
    while running:
          screen.fill("black")

          choose_category_text = font2.render("Press a number to choose a category: ", True, "white")
          fruits = font2.render("0 - Animals", True, "white")
          animals = font2.render("1 - Fruits", True, "white")
          colours = font2.render("2 - Colours", True, "white")
          numbers = font2.render("3 - Numbers", True, "white")

          screen.blit(choose_category_text, (250, 125))
          screen.blit(fruits, (400, 200))
          screen.blit(animals, (400, 250))
          screen.blit(colours, (400, 300))
          screen.blit(numbers, (400, 350))



          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        input_choice = event.unicode.lower()

                        if input_choice.isalpha():
                              main_menu()
                        elif  input_choice.isdigit():
                              result = int(input_choice)
                              if result < 4:
                                   game()
                              else:
                                   main_menu()
                        else:
                             main_menu()


          pygame.display.update()


#word generator
def word_gen():
    global hidden_word 
    global guessed_word
    global category_title

    word = choose_category[result] #result is chosen category
    guessed_word = random.choice(word) #randomiser
    category_title = name_category[result] #title of chosen category
    hidden_word = ["_"] * len(guessed_word)  


     
#fonts
font1 = pygame.font.SysFont('times new roman',60)
font2 = pygame.font.SysFont('times new roman',30)
game_text = pygame.font.SysFont('times new roman',40)
menu_text = pygame.font.SysFont('times new roman', 80)
small_text = pygame.font.SysFont('times new roman', 20)

#def leaderboard():
def repeat():
     #this part resets the game values 
     global attempts
     global firekeeper_status
     global correct_guess
     global wrong_guesses
     global win_con
     global hidden_word
     
     running = True
     while running:
          screen.fill("dark green")

          #resetting game vars
          win_con = False
          word_gen()
          wrong_guesses.clear()
          attempts = 5
          firekeeper_status = 0
          
          
          
        
          
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()
                    
                    if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:

                                    win_con = False
                                    category()

                                elif event.key == pygame.K_ESCAPE:
                                     pygame.quit()
                                     running = False
                                     sys.exit()
                                     
                    

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
     global attempts
     global firekeeper_status
     global guessed_word
     global hidden_word
     global correct_guess
     global wrong_guesses
     global win_con
     global counter

     
     word_gen()
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
          def display_wrong_guesses():
              wrong_guesses_text = font2.render(f"wrong guesses: { ',' .join(wrong_guesses)}", True, "white")
               
          def display_guess_word():
              word_text = font1.render(" ".join(hidden_word), True, "white")
              screen.blit(word_text, (150,150))

          def display_attempts():
            attempts_surface = pygame.Surface((280,65))
            screen.blit(attempts_surface, (15,15))
            alphabet_only_text = small_text.render("Start guessing to save the witch", True, "grey")
            screen.blit(alphabet_only_text, (20, 55))
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
          
          def display_category():
            category_text = font1.render(str(category_title), True, "grey")
            screen.blit(category_text, (415,80))

          
          display_guess_word()
          display_attempts()
          display_wrong_guesses() ##-------S
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








          if attempts <= 0:
                display_lose()
                #firekeeper_status = 0 
                #if attempts < 0 :
                    #attempts +=  +1       
                win_con = True
                running = False
                counter += 1
                repeat()


          elif "_" not in hidden_word: 
                display_win()
                
                win_con = True
                running = False
                counter += 1
                repeat()
          
          
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
                    category()

        pygame.display.update()


main_menu()
    

        
    
    
    
        
    
    
    
