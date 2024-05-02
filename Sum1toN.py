#-------------------------------------------------------------------------
# Name:       Sum 1 to N
# Purpose:    Sum all numbers from 1 to a number specified by user
# Author:     Chen. C
# Created:    01/05/2024
#-------------------------------------------------------------------------

# Get number from user
n = int(input("Enter a number: "))

sum = 0

# Loop to sum from 1 to n
for i in range(1, n+1):
  sum += i

# Output results
print(f"The sum of all numbers from 1 to {n} is {sum}.")