number = 5
guesses = 5
win = False

while guesses > 0:
    num = int(input("Pick a number between 1 and 10:"))
    if num > 11:
        print("Woah to high!")
        guesses = guesses - 1
    elif num > number:
        print("The number is lower!")
        guesses = guesses - 1
    elif num < number:
        print("The number us greater")
        guesses = guesses - 1
    elif number == number:
        print("Omg! You did it!")
        guesses = 0




