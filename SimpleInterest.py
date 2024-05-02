#-------------------------------------------------------------------------
# Name:       Simple Interest
# Purpose:    Calculates the simple interest over t years
# Author:     Chen. C
# Created:    01/05/2024
#-------------------------------------------------------------------------

# Get info from user
principal = float(input("Enter the amount of money you want to invest (p): "))
rate = float(input("Enter the interest rate (r): "))
time = float(input("Enter the number of invested years (t): "))

# Calculate the interest for each year
for i in range(1, time+1):
  interest = round(principal * rate * time, 2)
  print(f"Year {1}: ${interest}")
