import random


words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
win = False
guesses = 8
secretWord = random.choice(words)
valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
guess_word = []
length_word = len(secretWord)
letter_storage = []
guesses_left = 8
letter_in_word = []
list_of_guesses = []

while guesses_left > 0:
    guess_word = []
    for character in secretWord:
        guess_word.append("_")
    print("There are %s letters in this word" % length_word)
    print(guess_word)
    guess = input("Enter a letter: ")
    if guess in letter_in_word:
        print("%s is in the word" % guess)
    if guess in secretWord:
        print("You guessed correctly!")
        for x in range(0, length_word):
            if secretWord[x] == guess:
                guess_word[x] = guess
                print(guess_word)

    else:
        print("%s is not in the word" % guess)

    guesses_left -= 1
    print("You have: ", guesses_left, "guesses so far")

    list_of_guesses.append(guess)
    print("Guesses made so far:", list_of_guesses)

    if guesses_left == 0:
        print("You ran out of guesses! :0!!")
