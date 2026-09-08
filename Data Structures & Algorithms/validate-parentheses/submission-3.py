class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ctoop = {'}': '{', ']': '[', ')': '('}

        for i in s:
            if i in ctoop:
                if stack and stack[-1] == ctoop[i]:
                    stack.pop()
                else:
                    return False  
            else:
                stack.append(i)
        if not stack:
            return True 
        else: 
            return False
            