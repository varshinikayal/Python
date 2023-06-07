def plusone(digits):
  #start from the rightmost digit
  i =len(digits)-1
  #increase the rightmost digit by 1
  digits +=1
  while digits[i] == 10:
    digits[i]=0
    i -= 1
    if 1 <0:
      digits.insert(0,1)
      break
     #Increment the current digit by 1
    digits[i] += 1
 return digits
nums = [1,2,9]
result = plusone(num)
print(result)
