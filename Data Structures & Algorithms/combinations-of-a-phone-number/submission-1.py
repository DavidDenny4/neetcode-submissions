class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        curr_stack = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(i):
            if i >= len(digits):
                res.append("".join(curr_stack))
            
            letters = mapping.get(i)
            for char in letters:
                curr_stack.append(char)
                helper(i + 1)
                curr_stack.pop()
        
        helper(0)
        return res
