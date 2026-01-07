for i in range(2):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list
for number in numbers:
    # If the number is even, skip it
    if number % 2 == 0:
        continue
    # Print the number if it’s odd
    print(number)

# List of numbers
numbers = [1, 4, 5, 7, 9, 10, 12]
# Loop through the list
for number in numbers:
    # Check if the number is a multiple of 3
    if number % 3 == 0:
        print(f"First multiple of 3 found: {number}")
        break  # Exit the loop
    print(f"{number} is not a multiple of 3")
print("Loop is terminated.")

# List of numbers
numbers = [1, 2, 3, 4, 5]
# Loop through the list
for number in numbers:
    if number % 2 == 0:
        # Placeholder for future code
        pass
    else:
        print(f"{number} is an odd number")