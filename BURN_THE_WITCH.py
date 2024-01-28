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
# 2. user login screen
# 3. leaderboard
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

#import images #chan
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
first_try = True
mini_loss = False
win = False
lose = False
chance = ["Yes"]
chance = random.choice(chance)

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
def blit_text(text, position, colour):
     text = font2.render(text, True, colour)
     screen.blit(text, position)


#categories to choose from #sofia
def category(level_categories):
    global result
    global input_choice
    
    input_choice = ''

    def input_choice_display():
        input_rect = pygame.Rect(375,150,200,50)
        pygame.draw.rect(screen, "white", input_rect,2)
        blit_text(input_choice, (input_rect.x + 5, input_rect.y + 5 ), "green")
         
    def blit_categories_dict(categories):
        blit_text("Type a category, hit ENTER: ", (325,100), "white")
        y_position = 225
        for i in categories_dict[categories]:
            blit_text(i,(425, y_position), "white")
            y_position += 50

    def error_message():
        blit_text("Input not in category, hit BACKSPACE to edit", (215,500), "red")

    wrong_input = False


    
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
                              wrong_input = True
                              break
                        if event.key == pygame.K_BACKSPACE:
                          input_choice = input_choice[:-1]
                        else:
                          input_choice += event.unicode.lower()
                        
            
          if wrong_input == True:
              error_message()

              
          pygame.display.update()

#word generator #chan
def word_gen():
    global hidden_word, guessed_word, category_title
    
    word = categories_lists[result] #result is chosen category
    guessed_word = random.choice(word) #randomiser
    category_title = result #title of chosen category
    hidden_word = ["_"] * len(guessed_word)  
    
#reset the game #chan
def reset():
     global win_con, mini_loss, correct_guess, wrong_guesses, attempts, firekeeper_status,chance, first_try, chance
     
     word_gen()
     #mini_gen()
     win_con = False
     mini_loss = False
     wrong_guesses.clear()
     correct_guess = 0
     first_try = True
     attempts = 5
     firekeeper_status = 0   
     chance = ["Yes", "No", "Yes", "No"]
     chance = random.choice(chance)

#def leaderboard():

def create_user_profile():
    global profile
    profile_input = ''
    
    def input_box(text,xPos,yPos,xRec,yRec):
        input_rect = pygame.Rect(xPos,yPos,xRec,yRec)
        pygame.draw.rect(screen, "white", input_rect,2)
        blit_text(text, (input_rect.x + 5, input_rect.y + 5 ), "green")
           
     
    running = True
    while running:
          screen.fill("black")
          input_box(profile_input,200,240,570,50)
          blit_text("type your profile: name | age | gender | faculty ", (200, 150), "white")
          blit_text("use SPACE to separate the info, hit enter to continue ", (190, 350), "grey")


          
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            profile = profile_input.split()
                            if len(profile) < 3:
                                break
                            else:
                                leaderboard() #chan please change to category("easy_categories")
                        if event.key == pygame.K_BACKSPACE:
                            profile_input = profile_input[:-1]
                        else:
                            profile_input += event.unicode.lower()

  


          pygame.display.update()

def leaderboard():
    global profile
    #maybe can save this info into leaderboard.txt too..?
    username = profile[0]
    age = profile[1]
    gender = profile[2]
    faculty = profile[3]
    
    

    running = True
    while running:
          screen.fill("black")
          blit_text(f"Username: {username}", (0,0), "white")
          blit_text(f"Age: {age}", (0,50), "white")
          blit_text(f"Gender: {gender}", (0,100), "white")
          blit_text(f"Faculty: {faculty}", (0,150), "white")
          

          
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()
                   
     



          pygame.display.update()

#chan
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
            if level == 1 or level == 4:
                subtext = small_text.render("Press enter to continue", True , "white")
                screen.blit(subtext, (380,300))

            if level == 2:
                subtext = small_text.render("You get engaged.", True , "white")
                screen.blit(subtext, (405,300))
            
            if level == 3:
                subtext = small_text.render("You and the firekeeper live happily ever after, congratulations.", True , "yellow")
                screen.blit(subtext, (225,300))

            if level == 5:
                subtext = small_text.render("You get engaged, again.", True , "white")
                screen.blit(subtext, (380,300))
            

            if level == 6:
                subtext = small_text.render("You and the firekeeper live happily ever after again, congratulations.", True , "yellow")
                screen.blit(subtext, (200,300))
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
                                    if level == 1 or level == 4:
                                        category("intermediate_categories")
                                    if level == 2 or level == 5:
                                        category("difficult_categories")
                                    if level == 3 or level == 6:
                                         main_menu()
                                    
                                         
                                         
                                elif event.key == pygame.K_ESCAPE:
                                     pygame.quit()
                                     running = False
                                     sys.exit()
                                     
                    

          pygame.display.update()
    #chan

def lose_screen():
     global win, lose, level
     

     level = 0
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
            subtext2 = small_text.render("Restart the game to restore the weave of fate, or persist in the doomed world you have created.", True, "red")
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


def easter_egg():
     
     
     running = True
     while running:
          screen.fill("black")
         
          counter = 0
          def egg():
            egg_text = "I will not let you ruin our marriage."
            egg = small_text.render(egg_text, 1, "red")
            screen.blit(egg, (330,270))
            close_text = "casting spell......"
            close = small_text.render(close_text, 1, "red")
            screen.blit(close,(405,310) )
          
                    
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()
                
                

          egg()
          pygame.display.update()                             
          pygame.time.delay(3000)
          pygame.quit()
          running = False
          sys.exit()   

#WINNIE
def mini_game():

     global attempts, firekeeper_status

# display variables
     width, height = 1000,600
     white = (255, 255, 255)
     black = (0, 0, 0)
   

# font
     font1 = pygame.font.Font("assets/Good Old DOS Smooth.ttf", 40)
     font2 = pygame.font.Font("assets/Gellisto.ttf", 40)
                
     screen.fill("black")
  

# to generate the random words ( will change the words later )
     def generate_word():
         word_list = ["sesquipedalianism", "trichotillomania", "incomprehensibility", "interdisciplinary",
                       "surreptitious", "hypothetically","floccinaucinihilipilification"]
         return random.choice(word_list)

# screen 1
     def main_screen():
         
         screen.fill(black)
 
         welcome_msg1 = font2.render("You thought it was over?", True, white)
         welcome_msg2 = font2.render("Defeat this Typing Challenge for a second chance!", True, white) 
         welcome_msg3 = font1.render("Press Enter to start", True, white)

         x_position1, y_position1 = 280,170
         x_position2, y_position2 = 40, 220
         x_position3, y_position3 = 260, 400
         screen.blit(welcome_msg1, (x_position1, y_position1))
         screen.blit(welcome_msg2, (x_position2, y_position2))
         screen.blit(welcome_msg3, (x_position3, y_position3))

         pygame.display.update()

         while True:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       return
                    
 # screen 2   
     def rule_screen():
         
         screen.fill(black)
 
         rule_msg1 = font2.render("RULES:", True, white)
         rule_msg2 = font2.render("1. You have 5 ATTEMPTS only", True, white) 
         rule_msg3 = font2.render("2. To win, retype all the words accurately", True, white)
         rule_msg4 = font2.render("3. You will lose immediately if you input wrongly", True, white)
         rule_msg5 = font1.render("Press Enter to continue", True, white)

         x_position1, y_position1 = 450,100
         x_position2, y_position2 = 40, 160
         x_position3, y_position3 = 27, 200
         x_position4, y_position4 = 35, 240
         x_position5, y_position5 = 200, 450
         screen.blit(rule_msg1, (x_position1, y_position1))
         screen.blit(rule_msg2, (x_position2, y_position2))
         screen.blit(rule_msg3, (x_position3, y_position3))  
         screen.blit(rule_msg4, (x_position4, y_position4)) 
         screen.blit(rule_msg5, (x_position5, y_position5)) 

         pygame.display.update()

         while True:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       return
    
# screen 3      
     def game_screen():
         global current_turn, win_msg, lose_msg, attempts, firekeeper_status, chance, mini_loss

# initializing
         user_input = ""
         current_turn = 0
         max_turns = 5
         win_msg = ""
         lose_msg = ""
         extra_msg = ""

         if current_turn < max_turns:
            current_word = generate_word()

# loop for game
         while True:
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                 elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:

                         if user_input == current_word:
                             current_turn += 1
                             current_word = generate_word()
                             user_input = ""
                             if current_turn == max_turns:
                                 win_msg = "Congrats! You win a second chance"
                                 user_input = ""

                                 
                             else:
                                 current_word = generate_word()
                                 user_input = ""
                         else:
                             lose_msg ="That's incorrect! You lose BIG time"
                             
                             mini_loss = True
                            

                     elif event.key == pygame.K_BACKSPACE:
                         user_input = user_input[:-1]
                     else:
                         user_input += event.unicode.lower()
                
    # for output message
             if win_msg:
                 output_surface = font2.render(win_msg, True, white)
             elif lose_msg:
                 output_surface = font2.render(lose_msg, True, white)
             else: 
                 output_surface = font2.render("", True, white)

             screen.fill(black)

    # render user input
             input_surface = font1.render(user_input, True, white)
             input_rect = input_surface.get_rect(center=(width // 2, height // 2 ))
             screen.blit(input_surface, input_rect)

    # render target text 
             target_surface = font1.render(current_word, True, white)
             target_rect = target_surface.get_rect(center=(width // 2, height // 4))
             screen.blit(target_surface, target_rect)

     # render user output
             x_position, y_position = 190, 350
             screen.blit(output_surface, (x_position, y_position))

             pygame.display.update()

    # End of the game
             if current_turn == max_turns:
                win_msg = "Congrats! You win a second chance"
                pygame.display.update()
                pygame.time.delay(2000)
                attempts = 1
                firekeeper_status = 4
                chance = "No"
                game()
                 
             if mini_loss == True:
                 lose_msg ="That's incorrect! You lose BIG time"
                 pygame.display.update
                 user_input = ""
                 attempts = 0
                 firekeeper_status = 5
                 chance = "No"
                 pygame.time.delay(2000)
                 game()

     main_screen()
     rule_screen()
     game_screen()

def game():
     #bandaid solution
     global attempts, firekeeper_status, guessed_word, hidden_word, correct_guess, wrong_guesses, win_con , win, lose, level, first_try, chance

     if first_try == True:      
        word_gen()
        first_try = False

     wrong_input = False 
     
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
            screen.fill("black")
            win_surface= pygame.Surface((1000,300))
            screen.blit(win_surface, (0,400))
            pygame.time.delay(500)
            char_text = font2.render("Firekeeper", True, "grey")
            screen.blit(char_text, (50,420))
            win_text = dialogue_text.render('"AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"',True, "red")
            screen.blit(win_text, (50,450))

          def display_win():
            global level
            screen.fill("black")
            win_surface= pygame.Surface((1000,300))
            screen.blit(win_surface, (0,400))
            pygame.time.delay(500)
            char_text = font2.render("Firekeeper", True, "grey")
            screen.blit(char_text, (50,420))
            if level == 0:  
                win_text = dialogue_text.render('"Thank you for saving me, you are now my best friend :)."', True, "light green")
            if level == 1:
                win_text = dialogue_text.render('"Thank you for saving me again, will you become my partner?"', True, "pink")
            if level == 2:
                win_text = dialogue_text.render('"Lets get married !"', True, "red") 
            if level == 3:
                win_text = dialogue_text.render('"Thank you for saving me."', True, "light green")
            if level == 4:
                win_text = dialogue_text.render('"Why do I keep getting kidnapped anyways??"', True, "white")
            if level == 5:
                win_text = dialogue_text.render('"This the part where we get married. Nobody will get between us."', True, "red")  
            screen.blit(win_text, (50,450))
 
          
          def display_category():
            category_text = font2.render(category_title, True, "white")
            screen.blit(category_text, (800,10))
          
          def error_message_2():
            blit_text("please type alphabets only", (350,500), "grey")
          
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
                                #sofia
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
                                else:
                                    wrong_input = True

          if wrong_input == True:
              error_message_2()
              
                                        
          #to display levels
          if level == 0 or level == 3:
               blit_text("level 1 : easy", (400, 10), "white")
          if level == 1 or level == 4:
               blit_text("level 2 : intermediate", (400, 10), "white")
          if level == 2 or level == 5:
               blit_text("level 3 : difficult", (400, 10), "white")
         
          #win/lose condition     
          if attempts <= 0:
                
                if chance == "Yes" and mini_loss == False:
                     mini_game()
                     
                     

                else:
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
                if level <6:
                     
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.time.delay(200)
                        create_user_profile()

                    elif level == 6:
                        easter_egg()
                     

        pygame.display.update()



main_menu()
pygame.quit()

    
    
