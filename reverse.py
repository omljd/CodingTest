#Write a Python function to reverse a string.	

# Input string
input_string = "Hello, World!"

# Initialize an empty string for the reversed result
reversed_string = ""

# Loop through the original string
for char in input_string:
    # Prepend each character to the reversed string
    reversed_string = char + reversed_string

# Print the original and reversed strings
print("Original String:", input_string)
print("Reversed String:", reversed_string)

#output:Original String: Hello, World!
#Reversed String: !dlroW ,olleH
