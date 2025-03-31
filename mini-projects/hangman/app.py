import questionary
import random

secret_words = [
    "Animal",
    "kite",
    "cat"
]

selected_word = secret_words[random.randint(0,len(secret_words)-1)]

# create a main function that takes the randmom word as argument and loop through word.len times. and implement hangman functionallity to this function