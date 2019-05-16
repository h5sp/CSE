import csv
with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    Fruits_total = 0
    Clothes_total = 0
    Meat_total = 0
    Beverages_total = 0
    Office_Supplies_total = 0
    Cosmetic_total = 0
    Snacks_total = 0
    Personal_total = 0
    Care_total = 0
    Household_total = 0
    Vegetables_total = 0
    Baby_total = 0
    Food_total = 0
    Cereal_total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        old_number = row[13]
        if row[2] == "Fruits":
            Fruits_total += float(old_number)
        if row[2] == "Clothes":
            Fruits_total += float(old_number)
        if row[2] == "Meat":
            Fruits_total += float(old_number)
        if row[2] == "Fruits":
            Fruits_total += float(old_number)
        if row[2] == "Fruits":
            Fruits_total += float(old_number)
        if row[2] == "Fruits":
            Fruits_total += float(old_number)
        if row[2] == "Fruits":
            Fruits_total += float(old_number)

