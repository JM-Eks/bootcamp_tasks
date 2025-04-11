# TASKS
# 1. Your task is to dynamically update the quantity of a supply item after a sale.
# 2. Request as much information from the user in order to know what product is to be sold.
# 3. Print out your inventory after each sale.
# 4. Create a shopping list of supplies that are low in stock (fewer than 10)
# 5. Find which animal type has the most variety. Variety in this case means the animal with the most headcount and number of breeds.



petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}

# Ask users what they want to buy and how much of it they want to buy
# chooseCategory = input("Please enter a category (dogs/cats/fish/food/toys/habitats): ")
# purchaseItem = input("Tell us what you want to buy: ")
# purchaseQuantity = int(input("Please enter the quantity of items you want to buy: "))

# Check that the item is in the inventory and there's enough stock to sell for the selected quantity


# Update and output the inventory to reflect new quantities of items after each sale
# Add any items from the supplies category with a quantity below 10 to the shopping list
# Find which animal has the most species and quantity