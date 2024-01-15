import pygame
import sys
import random

# initializing pygame
pygame.init()

# display variables
width, height = 400,500
white = (255, 255, 255)
black = (0, 0, 0)
font_size = 35

# font
font = pygame.font.Font(None, 36)

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

# repetition
current_turn = 0
turns = 5

while current_turn < turns:
      current_turn += 1
      user_input = ""
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
                    message1 = font.render(win_msg, True, black)
                else:
                    message2 = font.render(lose_msg, True, black)
                    user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                  user_input = user_input[:-1]
            else:
                 user_input += event.unicode

    screen.fill(white)

    # render user input
    input_surface = font.render(user_input, True, black)
    input_rect = input_surface.get_rect(center=(width // 2, height // 2 ))
    screen.blit(input_surface, input_rect)

    # render target text 
    target_surface = font.render(current_word, True, black)
    target_rect = target_surface.get_rect(center=(width // 2, height // 4))
    screen.blit(target_surface, target_rect)

    pygame.display.flip()
    clock.tick(30)

# End of the game
if pygame.time.get_ticks > 5:
   pygame.quit()
   sys.exit()
