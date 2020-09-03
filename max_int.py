# Program that finds the maximum positive integer input by a user. 
# The user repeatedly inputs numbers until a negative value is entered.

# Create two values to start the loop
num_int = 0
max_int = 0

# Compare each new input from user to the former and update the maximum as needed,
# until a negative value is entered
while num_int >= 0:
    num_int = int(input("Enter a positive integer: "))
    if num_int >= max_int:
        max_int = num_int

print("The maximum is", max_int)