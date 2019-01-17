import random
import string
words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
(random.choices(words))
(list(string.ascii_letters))

guesses = 8
win = False
secretWord = random.choice(words)
guess_word = []
length_word = len(secretWord)


while guesses > 0:
    num = int(input("Pick a number between 1 and 10:"))
    if secretWord > 11:
        print("Woah to high!")
        guesses = guesses - 1
    elif secretWord > number:
        print("The number is lower!")
        guesses = guesses - 1
    elif secretWord < number:
        print("The number is greater")
        guesses = guesses - 1
    elif secretWord == number:
        print("Omg! You did it!")
        guesses = 0
