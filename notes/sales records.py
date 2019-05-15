import csv
with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    List = []
    Name = "Fruits"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Fruits":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Fruits profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Clothes"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Clothes":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Clothes profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Meat"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Meat":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Meat profit was:")
    print("${:,}".format(total))

List.append(total)
print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Beverages"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Beverages":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Beverages profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Office Supplies"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Office Supplies":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Office Supplies profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Cosmetics"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Cosmetics":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Cosmetics profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Snacks"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Snacks":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Snacks profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Personal Care"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Personal Care":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Personal Care profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Household"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Household":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Household profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Vegetables"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Vegetables":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Vegetables profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Baby Food"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Baby Food":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Baby food profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    Name = "Cereal"
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == "Cereal":
            total += float(old_number)
            # print(old_number)

    total = round(total, 2)
    print("The total Cereal profit was:")
    print("${:,}".format(total))

List.append(total)

print("------------")


print("This is the most profitable is %s ")
print("${:,}".format(max(List)))


