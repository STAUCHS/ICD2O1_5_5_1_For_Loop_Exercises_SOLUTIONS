#-------------------------------------------------------------------------
# Name:       Dice Roll Sums
# Purpose:    Shows the sum result of 10 dice rolls
# Author:     Chen. C
# Created:    01/05/2024
#-------------------------------------------------------------------------

import random

for i in range(1, 11):
  # Generate random dice rolls
  roll1 = random.randrange(1, 7)
  roll2 = random.randrange(1, 7)

  # Add dice rolls
  sum = roll1 + roll2

  # Output results
  print(f"Roll {i}: {roll1} and {roll2} = {sum}")