class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def helper(curr_stack, open_count, close_count):
            
            if open_count == n and close_count == n:
                res.append("".join(curr_stack))
                return
            
            if open_count < n:
                curr_stack.append("(")
                helper(curr_stack, open_count + 1, close_count)
                curr_stack.pop()
            
            if open_count > close_count:
                curr_stack.append(")")
                helper(curr_stack, open_count, close_count + 1)
                curr_stack.pop()
            
        helper([], 0, 0)
        return res