class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if c in c_map and stack:
                if(c_map[c] != stack[-1]):
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        if len(stack) > 0:
            return False
        return True

