stack=[]
pairs={"(":")","{":"}","[":"]"}
for c in s:
  if (c in ["(","{","["):
            stack.append(c)
   elif(len(stack)==0):
            stack.pop()
            return false
 return stack==[]
