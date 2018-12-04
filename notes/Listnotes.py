# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black", "red", "purple", "silver", "grey", "gold"] # Use Square Brackets
print(colors)
print(colors[1])
print(colors[0])

# Length of the list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "Green"
print(colors)

# Looping through lines
for item in colors:
    print(item)

'''
1. Make a list with 7 items
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''

new_list = ["pizza", "hamburger", "tacos", "burritos", "pie", "tamales", "soup"]
new_list[2] = "drink"
print(new_list)
print("The last thing in the list is %s" % new_list[len(new_list) - 1])

# Slicing a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:1])
print(new_list[:4])


food_list = ["pizza", "hamburger", "tacos", "burritos", "pie", "tamales", "soup", "brownie", "salad", "sushi", "cake", "chicken",
             "rice", "beans", "cheese", "noodles", "fish", "meat", "carne asada"]
print(len(food_list))

# Adding stuff to a list
food_list.append("bacon")
food_list.append("eggs")
# Notice that everything is object.method(parameters)
print(food_list)


food_list.insert(1, "eggo waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)

"""
1. make a new list with 3 items
2. add a 4th item to the list
3. Remove one of the first three items from the list
"""

soda_list = ["coke", "fanta", "crush"]
print(len(soda_list))

soda_list.append("sprite")
print(soda_list)

soda_list.remove("coke")
print(soda_list)

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)


# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

for i in range(len(list1)):  # i goes through all indices
    if list[i] == "u":  # if we find a U
        list1.pop(i)  # remove the i-th index
        list1.insert(i, "*")  # Put a * there instead
"""
for character in list1:
    if character == "u":
    # replace with a *
    current_index = list1.index(character)
    list1.pop(current_index)
    list1.insert(current_index, "*")
"""

# Turn a list into a string
print("".join(list1))


# Funtion Notes
# a**2 + b**2 = c**2
def pythagorean(a, b):
    return (a**2 + b**2)**(1/2)

print(pythagorean(3, 4))
