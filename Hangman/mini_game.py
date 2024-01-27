import pygame
import sys
import random

def mini_game():
# initializing pygame
     pygame.init()

# display variables
     width, height = 500,500
     white = (255, 255, 255)
     black = (0, 0, 0)
     font_size = 35

# font
     font1 = pygame.font.Font("Good Old DOS Smooth.ttf", 36)
     font2 = pygame.font.Font("Gellisto.ttf", 20)
                
     screen = pygame.display.set_mode((width, height))
     pygame.display.set_caption("Welcome to the typing challenge")

# to generate the random words ( will change the words later )
     def generate_word():
         word_list = ["sesquipedalianism", "trichotillomania", "incomprehensibility", "interdisciplinary", "surreptitious", "hypothetically"]
         return random.choice(word_list)

# screen 1
     def main_screen():
         
         screen.fill(black)
 
         welcome_msg1 = font2.render("You thought it was over?", True, white)
         welcome_msg2 = font2.render("Defeat this Typing Challenge for a second chance!", True, white) 
         welcome_msg3 = font2.render("Press Enter to start", True, white)

         x_position1, y_position1 = 145,170
         x_position2, y_position2 = 30, 200
         x_position3, y_position3 = 155, 300
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
 
         rule_msg1 = font2.render("Rules:", True, white)
         rule_msg2 = font2.render("1. You have 5 ATTEMPTS", True, white) 
         rule_msg3 = font2.render("2. To win, retype all the words accurately", True, white)
         rule_msg4 = font2.render("3. You will lose immediately if you input wrongly", True, white)
         rule_msg5 = font2.render("Press Enter to continue", True, white)

         x_position1, y_position1 = 230,100
         x_position2, y_position2 = 20, 160
         x_position3, y_position3 = 17, 190
         x_position4, y_position4 = 15, 220
         x_position5, y_position5 = 140, 290
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
         global current_turn, win_msg, lose_msg

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
                             user_input = ""
                            
                     elif event.key == pygame.K_BACKSPACE:
                         user_input = user_input[:-1]
                     else:
                         user_input += event.unicode.lower()
                
    # for output message
             if win_msg:
                 output_surface = font2.render(win_msg, True, white)
                 screen.blit(output_surface, (90, 300))
                 pygame.display.update()
                 pygame.time.delay(2000)  # Display the message for 2 seconds
                 break  # Exit the game loop if the player wins
             elif lose_msg:
                  output_surface = font2.render(lose_msg, True, white)
                  screen.blit(output_surface, (90, 300))
                  pygame.display.update()
                  pygame.time.delay(2000)  # Display the message for 2 seconds
                  break  # Exit the game loop if the player loses
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
             x_position, y_position = 90, 300
             screen.blit(output_surface, (x_position, y_position))

             pygame.display.update()

    # End of the game
             if current_turn > max_turns :
                 pygame.quit()
                 sys.exit()


     main_screen()
     rule_screen()
     game_screen()


mini_game()
