# Prompt the user to enter a number
user_input = input("Enter a number to compute its factorial: ")

# Function to compute factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply the result by the current number (i)
    return result  # Return the factorial

# Convert user input to an integer directly
number = int(user_input)

# Check if the number is negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is: {factorial(number)}")
