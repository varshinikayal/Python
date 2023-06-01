class Solution:
   def isvalid(self, S: str) -> bool:
      #create a empty stack
      stack=[]
      #map the same type of brackets(key:values)
      pairs={"(":")","{":"}","[":"]"}
      #check the brackets 
      for c in s:
          if (c in ["(","{","["):
            stack.append(c)
       #check length of stack equals to zero and remove the last element
          elif(len(stack)==0):
            stack.pop()
            return false
       #If the stack finally get empty it is valid             
 return stack==[]
            
            
   
           

       
           
            
            
            
       
