import random
words = ["Crypt", "Wildebeest", "Cupcake", "Documents", "Awkward", "Croquet", "Fervid",
         " Bungler", "Rhythmic", "Zombie"]
print(random.choices(words))
guesses = 8
win = False
string1 = random.choice(words)
list1 = list(string1)
print()
