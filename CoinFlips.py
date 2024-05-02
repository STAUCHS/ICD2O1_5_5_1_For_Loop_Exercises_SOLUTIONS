#-------------------------------------------------------------------------
# Name:       Coin Flips
# Purpose:    Simulates a number of coin flips 
# Author:     Chen. C
# Created:    01/05/2024
#-------------------------------------------------------------------------

import random

# Output title
print("** Coin Flip Simulator **")

# Ask user for number of flips
num_of_flips = int(input("How many times do you want to flip the coin? "))

# Initialize variables
heads = 0
tails = 0

for i in range(num_of_flips):
  # Create a random flip - 0 for tails, 1 for heads
  flip = random.randrange(2)
  if flip == 1:
    heads += 1
  else:
    tails += 1

print(f"Number of Heads: {heads}")
print(f"Number of Tails: {tails}")