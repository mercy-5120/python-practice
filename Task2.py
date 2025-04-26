# Prompt the user to enter a number
user_input = input("Enter a number: ")

# Convert user input to integer directly
number = int(user_input)


# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:  # If the number is divisible by 2 with no remainder
        return "Even"
    else:
        return "Odd"

# Call the function and print the result
print(check_even_odd(number))  # Output the result (Even or Odd)
