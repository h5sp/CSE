import csv
with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
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

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
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

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
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

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
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

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
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
