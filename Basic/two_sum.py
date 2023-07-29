def twosum(nums,target)
   #create a empty dictionary
   num_map = {}
    #Iterate through indices and element of nums list
   for i, num in enumerate(nums):
    #calculate the difference target and current element
      values = target - num
    #check if the values exists in the dictionary
      if values in num_map:
        #If the values exits return the indix and current element
        return [num_map[values], i]
      #If the complement doesn't exists add current element and its index to num_map
      num_map[num] = i
      #If there is no solution is found return empty list
    return []
nums = [2,7,11,15]
target = 9
#call twosum function with nums list and the target element
result = twosum(nums,target)
#print the result
print(result)
