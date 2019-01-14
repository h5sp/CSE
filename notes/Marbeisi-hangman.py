import random

words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid", " Bungler", "Rhythmic", "Zombie"]
print(random.choices(words))

guess_word = []

secretWord = random.choice(words)

length_word = len(secretWord)

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_storage = []
