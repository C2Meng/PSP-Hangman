import pygame, sys
import random
# from list import easy_categories_list #revision to be made on lists to import

pygame.init()
FPS = 60
clock = pygame.time.Clock()


#create screen
Background=pygame.image.load("assets/background2.jpg")
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption ("Hangman")

#Status progression// images 
status_png = [0,1,2,3,4,5]
status_png[0] = pygame.image.load("assets/firekeeper0.png")
status_png[1] = pygame.image.load("assets/firekeeper1.png")
status_png[2] = pygame.image.load("assets/firekeeper2.png")
status_png[3] = pygame.image.load("assets/firekeeper3.png")
status_png[4] = pygame.image.load("assets/firekeeper4.png") 
status_png[5] = pygame.image.load("assets/firekeeper5.png")  

#game status
firekeeper_status = 0
correct_guess = 0
attempts = 5

#colour
white = (255,255,255)
black = (0,0,0)
#font
font1 = pygame.font.Font(None,60)
font2 = pygame.font.Font(None,30)

#user input
input_letter = ''

#words list
word = ["applepie","car","pizza","popular"]
guessed_word = random.choice(word)
hidden_word = ["_"] * len(guessed_word)

#displays
def display_guess_word():
    word_text = font1.render(" ".join(hidden_word), True, white)
    screen.blit(word_text, (300,200))

def display_attempts():
    attempts_surface = pygame.Surface((180,30))
    screen.blit(attempts_surface, (15,15))
    attempts_text = font2.render(f"Attempts left:  {attempts}", True, white)
    screen.blit(attempts_text, (20,20))

def display_lose():
    lose_text = font1.render("YOU LOSE!", True, white)
    screen.blit(lose_text, (300,100))

def display_win():
    lose_text = font1.render("YOU WIN!", True, white)
    screen.blit(lose_text, (300,100))


 

#game loop
running = True
while running:
    screen.blit(Background, (0,0))
    screen.blit(status_png[firekeeper_status],(70,200))
    clock.tick(FPS)

    display_attempts()
    display_guess_word()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_letter = input_letter[:-1]
            else:
                input_letter = event.unicode.lower()

                # Check if the letter is in the guessed word
                if input_letter in guessed_word:
                    for i in range(len(guessed_word)):
                        if guessed_word[i] == input_letter:
                            hidden_word[i] = input_letter
                            correct_guess += 1           
                else:
                    attempts -= 1
                    firekeeper_status += 1
                    
    
    if attempts <= 0:
        display_lose()
    elif correct_guess == len(guessed_word):
        display_win()

        
        
    
    pygame.display.update()
    
    

        
    
    
    
