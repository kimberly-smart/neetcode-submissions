class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False
        
        pairdict = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in pairdict:
                if stack and stack[-1] == pairdict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    
        return True if not stack else False
