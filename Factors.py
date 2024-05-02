#-------------------------------------------------------------------------
# Name:       Factors
# Purpose:    Outputs the all factors of a positive integer
# Author:     Chen. C
# Created:    01/05/2024
#-------------------------------------------------------------------------

# Get positive integer form user
num = int(input("Enter a positive integer: "))

print(f"The factors of {num} are: ")

# Check the divisibility of each number from 1 to num
for i in range(1, num+1):
  if num % i == 0:
    print(i)