def length_of_last_word(s)
   #remove the whitespaces
   s = s.strips()
   #check the string is empty after removing whitespaces
   if not s:
      return 0
   #split the string into words
   words = s.split()
   #return the length of the last word
   return len(words[-1])
   string = "Hello world"
   result = length_of_last_word(string)
   print(result)
