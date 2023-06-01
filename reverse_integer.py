def reverse_signed(num)
 #Initialize the sum=0 and sign=1
  sum = 0
  sign = 1
  #check the num value is < tha zero or >than zero
   if num < 0:
     sign = -1
     num = num *-1
   while num > 0:
       rem = num % 10
       sum = sum * 10 + rem
       num = num // 10
     #check the range 
    if not -2147483648 <sum< 2147483647:
       return 0
    return sign * sum 
 #Call the function
 print(reverse_signed(234))
  
