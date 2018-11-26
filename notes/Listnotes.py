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
