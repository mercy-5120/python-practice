# Function to compute factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive case

number = int(input("Enter a number to compute its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is: {factorial_recursive(number)}")
