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
clock = pygame.time.Clock()

# to generate the random words ( will change the words later )
def generate_word():
    word_list = ["meow", "woof", "moo"]
    return random.choice(word_list)

def play_game(turns):
    global current_turn
    current_turn = 0

# initializing
win_msg = ""
lose_msg =""
user_input = ""

# Set the number of turns
turns = 5
current_turns = 0

while current_turn < turns:
      current_turn += 1
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
                    current_word = generate_word()
                    if current_turn < turns:
                        current_turn += 1
                    else:
                    win_msg = "Congratulations!"
                 user_input = ""
                else:
                    lose_msg = "Uh Oh! No hint for you"
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                  user_input = user_input[:-1]
            else:
                 user_input += event.unicode
                

    # for output message
    if "win_msg":
        output_surface = font2.render(win_msg, True, white)
    elif "lose_msg":
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


    pygame.display.flip()
    clock.tick(30)

    # End of the game
    if pygame.time.get_ticks() > 10000:
       pygame.quit()
       sys.exit()
