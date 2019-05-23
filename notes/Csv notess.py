import csv


def validate(num: str):
    if not all_16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print("Not every number has 16 digits!!")
        return False

# with open("Book1.csv") as old_csv:
# with open("MyNewFile.csv", 'w', newline='') as new_csv:
# print("Writing file.....   ")
# reader = csv.reader(old_csv)
# writer = csv.writer(new_csv)
# for row in reader:
# old_number = int(row[0])
# new_number = old_number + 1
# row[0] = new_number
# writer.writerow(row)
# print(int(old_number) + 1)
# print(old_number)
# print("OK")

# with open("Book1.csv", 'r') as old_csv:
# with open("MyNewFile.csv", 'w', newline='') as new_csv:
# reader = csv.reader(old_csv)
# writer = csv.writer(new_csv)
# #print("Processing....")
# for row in reader:5
#  first_num = int(old_number[0])  # This is the first number
# if first_num % 2 == 0:
#  writer.writerow(row)
# print(int(old_number) + 1)
# print(old_number)
# print("Done")


def reverse_it(string):
    print(string[::-1])


reverse_it("Hello World")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing....")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_num = row[0]
            if validate(old_num):
                writer.writerow(row)
print("Done")

playing = True

directions = ['north', 'south', 'west', 'east', 'up', 'down', 'south_east', 'north_west', 'north_east', 'south_west',
              'east_north', 'east_south']

while playing:
    print("-", ME.current_location.name)
    print("-", ME.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit', 'e']:
        playing = False
        if command.lower() in directions:
            try:
                room_name = getattr(ME.current_location, command.lower())
                ME.move(room_name)
            except KeyError:
                print("Error: Can't go that way")
        else:
            print("cant go that way")
