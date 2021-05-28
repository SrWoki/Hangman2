# Import modules to use
from words import words
import random
from colorama import Fore,Style


# 1. Welcome
print("Welcome to the game hangman in Python")

# 2. Function to get word
def get_valid_word(words):
  word = random.choice(words)

  # Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(words)

  return word

# Display word and its length
my_word = get_valid_word(words)
print(my_word + '\n',len(my_word))

# Una función que despliegue los guiones
# dependiendo el tamaño de la palabra
# Ejemplo:
# A N O N Y M O U S
# _ _ _ _ _ _ _ _ _

print(Fore.RED+"-"*len(my_word))