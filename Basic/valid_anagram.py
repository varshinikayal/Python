def is_anagram(s, t):
    # Check if the sorted versions of strings 's' and 't' are equal.
  
    return sorted(s) == sorted(t)

# Example usage:
s = "anagram"
t = "nagaram"

result = is_anagram(s, t)
# Print the result
print(result)  # Output: True
