def removeduplicates(nums):
  #check tje array is empty or not
  if len(nums)==0:
    return 0
  #initialize the pointer
  pointer=0
  #iterate the array
  for i in range(1, len(nums)):
    #compare the current element with the element at pointer
    if nums[i] != nums[pointer]:
      pointer +=1
      #update the element at the pointer with current element
      nums[pointer] = nums[i]
   return pointer + 1
nums =[1,1,2]
#call the function
result = removeduplicates(nums)
#The array after removing duplicates will be [1,2,_]
#The function returns 2
print(result) #output: 2
