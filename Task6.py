# Prompt the user to enter a number
user_input = int(input("Enter a number: "))

# Function to sum the digits of a number
def sum_of_digits(number):
    total = 0  # Initialize the total sum to 0

    while number > 0:
        digit = number % 10  # Get the last digit
        total += digit  # Add the digit to the total
        number = number // 10  # Remove the last digit
    return total

# Display the sum of the digits
print(f"Sum of the digits: {sum_of_digits(user_input)}")
