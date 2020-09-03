# Program that generates the first n numbers in the sequence:; 1, 2, 3, 6, 11, 20, 37, ...
# Each number is the sum of the three numbers before.

n = int(input("Enter the length of the sequence: "))

# Initialize the values that will be summed up in the loop
first_int = 1
second_int = 2
third_int = 3

# Print the first three numbers in the sequence
print(first_int)
print(second_int)
print(third_int)

# Run a loop that prints n sums of three integers, updating the integers
# according to the sequence each time
for i in range(2,n):
    next_int = first_int + second_int + third_int
    print(next_int)
    first_int = second_int
    second_int = third_int
    third_int = next_int
    