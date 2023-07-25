def find_missing_number(nums)
#Get the length of input array 'nums'
n = len(nums)

#calculate the sum of consecutive integers
sum1 = (n* (n + 1)) // 2

#Using sum function calculate the sum of elements in nums 
sum2 = sum(nums)

#subtract sum1 is a actual value from sum2 is the excepted value to find missing number
missing_number = sum1 - sum2
return missing_number

