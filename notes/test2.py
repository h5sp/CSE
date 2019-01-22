import random
import sys


# lets set some variables
wordList = ["crypt", "wildebeest", "cupcake", "documents", "awkward", "croquet", "fervid",
         "bungler", "rhythmic", "zombie"]

guess_word = []
secretWord = random.choice(wordList) # lets randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def newFunc():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gameChoice = input("Would You?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue
newFunc()

def change():

    for character in secretWord:
        guess_word.append("*")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)




def guessing():
    guess_taken = 1

    while guess_taken < 8:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '*' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was",         secretWord)



change()
guessing()

print("Game Over!")