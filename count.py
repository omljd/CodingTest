"""Write a Python function to count the occurrences of a
specific element in a list."""

# Define the list and the element to count
my_list = [1, 2, 3, 4, 2, 2, 5, 2, 6]
element_to_count = 2

# Initialize the count variable
count = 0

# Loop through the list and count occurrences of the element
for item in my_list:
    if item == element_to_count:
        count += 1

# Print the result
print(f"Element {element_to_count} occurs {count} times in the list.")


#Output:-Element 2 occurs 4 times in the list.
