def ispalindrome(x)
  #convert the int to str
  num_str=str()
  #reverse the string using slicing
  reversed_str = num_str[::-1]
  #compare the original string and reversed string
  if (num_str == reversed_str):
     return True
  else:
    return False
nums = 121
result = ispalindrome(nums)
print(result)
