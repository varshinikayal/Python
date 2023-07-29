def reverseString(s):
    # Slice the list 's' with [::-1] to create a reversed copy of the list.
    # The syntax 's[::-1]' means to start from the end of the list and step backwards with a step size of -1
    s[:] = s[::-1]

# Example usage:
# Create a list 'input_string' with characters 'h', 'e', 'l', 'l', 'o'.
input_string = ['h', 'e', 'l', 'l', 'o']
# Call the 'reverseString' function with 'input_string' as the argument.
reverseString(input_string)
# The output will be ['o', 'l', 'l', 'e', 'h'], as the list has been reversed in place.
print(input_string)  # Output: ['o', 'l', 'l', 'e', 'h']
