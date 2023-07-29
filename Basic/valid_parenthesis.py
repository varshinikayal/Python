class Solution:
    def isvalid(self, S: str) -> bool:
        # Create a empty stack
        stack = []
        # Map the same type of brackets (key:values)
        pairs = {"(": ")", "{": "}", "[": "]"}
        
        # Check the brackets
        for c in S:  
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                # Check if the stack is empty before trying to pop an element
                if len(stack) == 0:
                    return False
                # Compare the current closing bracket with the corresponding opening bracket
                if pairs[stack.pop()] != c:
                    return False
        
        # Check if the stack is empty after processing all characters
        return len(stack) == 0
