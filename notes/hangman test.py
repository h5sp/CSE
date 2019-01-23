import random
import string

words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
print(list(string.ascii_letters))
print(random.choice(words))
win = False
guesses = 8
secretWord = random.choice(words)
guess_word = []
length_word = len(secretWord)
letter_storage = []
