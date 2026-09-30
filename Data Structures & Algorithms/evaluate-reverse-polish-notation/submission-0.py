class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) < 2:
            return int(tokens[0])
        
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                second = stack.pop()
                first = stack.pop()
                if tokens[i] == "+":
                    stack.push(first + second)
                elif tokens[i] == "-":
                    stack.push(first - second)
                elif tokens[i] == "*":
                    stack.push(first * seocnd)
                else:
                    stack.push(first / second)
            else:
                stack.push(int(tokens[i]))
        
        return stack[-1]