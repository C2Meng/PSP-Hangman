import pygame
import sys
import random

# initializing pygame
pygame.init()

# display variables
width, height = 400, 500
white = (255, 255, 255)
black = (0, 0, 0)
font_size = 35

# win and lose
win_msg = "Congratulations! Here's ya hint"
lose_msg = "Oy tough luck! Try again next time"

# set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to the typing challenge")
clock = pygame.time.Clock()

# font
font = pygame.font.Font(None, 36)

# to generate the random words ( will change the words later )
def generate_word():
    word_list = ["meow", "woof", "moo"]
    return random.choice(word_list)
    
# how many times to play
turns = 4
current_turn = 1

# loop for game
while current_turn < turns:
    current_turn = current_turn + 1

user_input = ""
current_word = generate_word()

for event in pygame.event.get():
       if event.type == pygame.QUIT
           pygame.quit()
           sys.exit()
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RETURN:
               if user_input == curent_word:
                  message1 = font.render(win_msg, black)
               else:
                  message2 = font.render(lose_msg, black)
                  user_input = ""
           elif event.key == pygame.K_BACKSPACE:
               user_input = user_input[:-1]
           else:
               user_input += event.unicode
           
screen.fill(white)

# render user input
input_surface = font.render(user_input, black)
input_rect = input_surface.get_rect(center=(width // 2, height // 2 ))
screen.blit(input_surface, input_rect)

# render target text
target_surface = font.render(current_word, black)
target_rect = target_surface.get_rect(center=(width // 2, height // 4 ))
screen.blit(target_surface, target_rect)

# pausing before next iteration
pygame.time.delay(2000)

# end of the game
pygame.quit()
sys.exit()


        

