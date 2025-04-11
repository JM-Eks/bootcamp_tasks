# TASKS

# A fast-food restaurant takes customer orders and stores them in a tuple to ensure they remain unchanged once confirmed.

# Instructions:
# 1. Create a tuple named order that contains the following items: ("Burger", "Fries", "Soda"). ✅
# 2. The restaurant now offers a "Super Meal" combo, which includes an additional "Ice Cream". However, tuples are immutable! ✅
# 3. Convert the tuple into a list, add "Ice Cream", and convert it back into a tuple. ✅
# 4. Print the modified tuple to confirm the update. ✅
# 5. Retrieve and print the first and last items in the order using their index positions. ✅

orderMenu = ("Burger", "Fries", "Soda")
orderMenu_list = list(orderMenu)
orderMenu_list.append("Ice cream")
newOrderMenu = tuple(orderMenu_list)

# print(newOrderMenu)

firstAndLastItems = newOrderMenu[::3]

print("A tuple of the first and last items in the updated order menu")
print(firstAndLastItems)

print("")

print("A tuple of the first and last items in the updated order menu printed as a string")
print(", ".join(firstAndLastItems))
