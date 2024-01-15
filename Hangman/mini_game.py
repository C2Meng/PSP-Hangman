import pygame
import sys
import random

# initializing pygame
pygame.init()

# display variables
width, height = 200
white = (500, 500, 500)
black = (0, 0, 0)
font_size = 35

# win and lose
win_msg = "Congratulations! Here's ya hint"
lose_msg = "Oy tough luck! Try again next time"

# set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to the typing challenge")
clock = pygame.time.Clock()

# to generate the random words ( will change the words later )
def generate_word():
    word_list = ["meow", "woof", "moo"]
    return random.choice(word_list)

# to output the random word
def main():
    user_input = " "
    current_word = generate_word()

# loop for game
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

# render user input
input_surface = font.render(user_input, black)
input_rect = input_surface.get.rect(center=(width // 2, height // 2 ))
screen.blit(input_surface, input_rect)



        

