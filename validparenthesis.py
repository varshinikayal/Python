Method 1

stack=[]
pairs={"(":")","{":"}","[":"]"}
for c in s:
  if (c in ["(","{","["):
            stack.append(c)
   elif(len(stack)==0):
            stack.pop()
            return false
 return stack==[]
            
            
   Method-2
           
stack=[]
d={"(":")","{":"}","[":"]"}
for i in s:
  if i in  d.keys():
      stack.append(i)
  else:
      if stack==[]:
            return 0
   else:
       if d[stack[-1]]==i:
            stack.pop()
    else:
       return 0
   if stack ==[]:
       return 1
   else:
       return 0     
       
           
            
            
            
       
