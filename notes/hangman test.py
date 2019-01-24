import random
import string

words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
(list(string.ascii_letters))
(random.choice(words))
win = False
guesses = 8
secretWord = random.choice(words)
guess_word = []
length_word = len(secretWord)
letter_storage = []
guesses_left = 8
letter_in_word = []
list_of_guesses = []

while guesses_left > 0:
    guess = input("Enter a letter: ")

    if guess in letter_in_word:
        print("%s is in the word" % guess)
    else:
        print("%s is not in the word" % guess)

    guesses_left -= 1
    print("You have: ", guesses_left, "guesses so far")

    list_of_guesses.append(guess)
    print("Guesses made so far:", list_of_guesses)

    if guesses_left == 0:
        print("You ran out of guesses! :0!!")
