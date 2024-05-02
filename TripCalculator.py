#-------------------------------------------------------------------------
# Name:       Trip Calculator
# Purpose:    Calculates the total distance 
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# Get number of trips from user
num_of_trips = int(input("Enter the number of trips: "))

total_distance = 0

# Update total distance based on user input
for i in range(num_of_trips):
  distance = float(input(f"Enter the distance travelled for trip {i+1}: "))
  total_distance += distance

# Output the total distance
print(f"\nThe total distance travelled in your trips is: {total_distance} km.")