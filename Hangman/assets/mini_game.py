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

# set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_captions("Welcome to the typing challenge")
clock = pygame.time.Clock()

# to generate the random words
def generate_word():
    word_list = ["meow", "woof", "moo"]
    return random.choice(word_list)

# to output the random word
def main():
    user_input = " "
    current_word = generate_word()

# loop for game
    while 

