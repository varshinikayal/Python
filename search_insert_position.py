def serachinsert(nums,target):
   left = 0
    right = len(nums)-1
    while left <=right:
      mid = (left + right) // 2
      #check if the target is found
      if nums[mid] == target:
        return mid
      #check if the target is smaller,search the left half
      elif nums[mid] > target:
        right = mid -1
      #check if the target is larger, search the right half
      else:
        left = mid
        #If target is not found,return the insertion index
     return left
  
  nums = [1,3,5,6]
  target = 4
  index = searchinsert(nums,target)
  print(index)
      
