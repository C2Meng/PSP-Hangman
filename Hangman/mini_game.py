import pygame
import sys
import random

# initializing pygame
pygame.init()

# display variables
width, height = 500,500
white = (255, 255, 255)
black = (0, 0, 0)
pale_blue = (172, 223, 221)
font_size = 35

# font
font1 = pygame.font.Font("Good Old DOS Smooth.ttf", 36)
font2 = pygame.font.Font("Gellisto.ttf", 20)

# set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to the typing challenge")


# to generate the random words ( will change the words later )
def generate_word():
    word_list = ["meow", "woof", "moo", "bagel", "chocolate", "vanilla"]
    return random.choice(word_list)

# initializing
user_input = ""
current_turn = 1
max_turns = 5
win_msg = ""
lose_msg = ""
extra_msg = ""

def playing_game():
    global current_turn, win_msg, lose_msg

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

                #sep
                    if user_input == current_word:
                        current_turn += 1
                        current_word = generate_word()
                        user_input = ""
                    elif current_turn == max_turns:
                        win_msg = f"Yay! You won in {current_turn} turns!"
                        user_input = ""
                    else:
                        lose_msg = f"Uh oh! You lost in {current_turn} turns" 
                        user_input = ""

            elif event.key == pygame.K_BACKSPACE:
                  user_input = user_input[:-1]
            else:
                 user_input += event.unicode
                

    # for output message
    if win_msg:
        output_surface = font2.render(win_msg, True, white)
    elif lose_msg:
        output_surface = font2.render(lose_msg, True, white)
    elif extra_msg:
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
    x_position, y_position = 200,50
    output_rect = output_surface.get_rect(center=(width // 2, height // 4))
    screen.blit(output_surface, (x_position,y_position))

    pygame.display.update()

    # End of the game
    if current_turn > max_turns:
       pygame.quit()
       sys.exit()

playing_game() 
