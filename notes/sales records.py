import csv
with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    Fruits_total = 0
    Clothes_total = 0
    Meat_total = 0
    Beverages_total = 0
    Office_Supplies_total = 0
    Cosmetics_total = 0
    Snacks_total = 0
    Personal_Care_total = 0
    Household_total = 0
    Vegetables_total = 0
    Baby_Food_total = 0
    Cereal_total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        old_number = row[13]
        if row[2] == "Fruits":
            Fruits_total += float(old_number)
        if row[2] == "Clothes":
            Clothes_total += float(old_number)
        if row[2] == "Meat":
            Meat_total += float(old_number)
        if row[2] == "Beverages":
            Beverages_total += float(old_number)
        if row[2] == "Office Supplies":
            Office_Supplies_total += float(old_number)
        if row[2] == "Cosmetics":
            Cosmetics_total += float(old_number)
        if row[2] == "Snacks":
            Snacks_total += float(old_number)
        if row[2] == "Personal Care":
            Personal_Care_total += float(old_number)
        if row[2] == "Household":
            Household_total += float(old_number)
        if row[2] == "Vegetables":
            Vegetables_total += float(old_number)
        if row[2] == "Baby Food":
            Baby_Food_total += float(old_number)
        if row[2] == "Cereal":
            Cereal_total += float(old_number)

total = round(Fruits_total, 2)
print("The total Fruits profit was:")
print("${:,}".format(total))

print("---------------")

total = round(Clothes_total, 2)
print("The total Clothes profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Meat_total, 2)
print("The total Meat profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Beverages_total, 2)
print("The total Beverages profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Office_Supplies_total, 2)
print("The total Office Supplies profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Cosmetics_total, 2)
print("The total Cosmetics profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Snacks_total, 2)
print("The total Snacks profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Personal_Care_total, 2)
print("The total Personal Care profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Household_total, 2)
print("The total Household profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Vegetables_total, 2)
print("The total Vegetables profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Baby_Food_total, 2)
print("The total Baby food profit was:")
print("${:,}".format(total))

print("---------------")


total = round(Cereal_total, 2)
print("The total Cereal profit was:")
print("${:,}".format(total))

print("---------------")


list_of_profits = [Fruits_total, Clothes_total, Meat_total, Beverages_total, Office_Supplies_total, Cosmetics_total,
                   Snacks_total, Personal_Care_total, Household_total, Vegetables_total, Baby_Food_total, Cereal_total]

list_of_items = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal Care",
                 "Household", "Vegetables", "Baby Food", "Cereal"]

index_of_items = list_of_profits.index(max(list_of_profits))
print("The most amount of profit is: ", ("${:,}".format(max(list_of_profits)), list_of_items[index_of_items]))
