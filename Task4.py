# Prompt the user to enter a string
user_input = input("Enter a string to reverse: ")

# Function to reverse a string
def reversed_string(input_string):
    reversed_string = ""  # Initialize an empty string for the reversed string
    for char in input_string:
        reversed_string = char + reversed_string  # Add the character at the beginning of the reversed string
    return reversed_string  # Return the reversed string

# Call the function and print the reversed string
reversed_str = reversed_string(user_input)
print(f"Reversed string: {reversed_str}")
