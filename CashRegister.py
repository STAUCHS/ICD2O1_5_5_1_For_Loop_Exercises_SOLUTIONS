#-------------------------------------------------------------------------
# Name:       Cash Register
# Purpose:    Calculates the total price with tax
# Author:     Chen. C
# Created:    01/05/2024
#-------------------------------------------------------------------------

# Get number of items from user
num_of_items = int(input("How many items do you want to buy? "))

subtotal = 0

# Ask user for price and quantity of each item
for i in range(1, num_of_items + 1):
  price = float(input(f"Enter the price of item {i}:"))
  quantity = int(input(f"Enter the quantity of item {i}: "))

  # Add to subtotal
  subtotal += price * quantity

# Calculate with tax
total = subtotal * 1.13

print(f"The total price including tax is ${total}")