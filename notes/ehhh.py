number = input("Enter the number: ")

numbers = map(int, str(number))

last = numbers[:-1]

rev = list(reversed(numbers[::-1]))

multiplied = [i*2 if j % 2 == 0 else i for j, i in enumerate(rev)]
