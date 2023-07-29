def string_to_integer(s):
    try:
        # To convert the input string 's' to an integer using the int() function.
        return int(s)
    except ValueError:
        # If the int() function raises a ValueError , the program will jump to this 'except' block.
         print("Error: The input string is not a valid integer.")
         return None

# Example usage:
# Define the input string as "123".
input_string = "123"
# Call the 'string_to_integer' function with 'input_string' as the argument.
result = string_to_integer(input_string)
# Check if the 'result' is not 'None' (i.e., the conversion was successful).
if result is not None:
    # If the conversion was successful, print the resulting integer value.
    print("Converted integer:", result)
