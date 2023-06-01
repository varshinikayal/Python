#Function to divide a by b a and return floor value
def divide(dividend,divisor):
  #calculate the sign of divisor
  #sign will be negative only if either one of them is negative
  # otherwise it will be positive
  sign = -1 if ((divident<0) ^ (divisor < 0)) else 1
  #update both the divisor and dividend positive
  dividend = abs (dividend)
  divisor = abs (divisor)
  #Initialize the quotient
  quotient = 0
 while (dividend >= divisor):
    dividend -= divisor
    quotient += 1
    #If the sign value is -1 then
    #negate the value of quotient
 if sign == -1:
    quotient = - quotient
 return quotient
