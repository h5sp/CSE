import random
import string
words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
(random.choices(words))
print(list(string.ascii_letters))

guesses = 8
win = False
string1 = random.choice(words)
list1 = list(string1)
print()

