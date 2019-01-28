import random


words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
win = False
guesses = 8
secretWord = random.choice(words)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
guess_word = []
length_word = len(secretWord)
letter_storage = []
guesses_left = 8
letter_in_word = []
list_of_guesses = []
guess_taken = []

