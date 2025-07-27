# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while
while row < size:
    # Inner loop using for to print asterisks in the row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after a row is complete
    row += 1
