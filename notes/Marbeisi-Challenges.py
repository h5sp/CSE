# challenge1
def challenge1(first_name, last_name):
    return last_name + ", " + first_name


name1 = challenge1("Marbeisi", "Morales")
print(name1)

# challenge2
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# challenge3

b = int(input("Input the base :"))
h = int(input("Input the height :"))

# challenge4
num = float(input("Enter a number: "))
if num > 0:
    print("Zero")
elif num == 0:
    print("Zero")
else:
    print("Negative number.")
# challenge5
r = 3
area = 3.14 * r ** 2
print(area)

# challenge 6
r = 5
volume = 1.33 * 3.44 * r ** 3
print(volume)

# challenge 7
n = 3
value = n + (n * n) + (n * n * n)

# challenge 8


# challenge 9


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))
print(is_vowel('c'))
print(is_vowel('c'))
