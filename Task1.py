# Function to sum all elements in a list
def sum_list(numbers):
    total = 0  # Initialize total to 0
    for num in numbers:  # Loop through each number in the list
        total += num  # Add each number to the total
    return total  # Return the total sum

print(sum_list([1, 2, 3, 4, 5]))
# Output: 15
