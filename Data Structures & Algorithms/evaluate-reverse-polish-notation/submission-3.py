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
                    stack.append(first + second)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(first * second)
                else:
                    stack.append(first / second)
            else:
                stack.append(int(tokens[i]))
        print(f"stack is {stack}")
        return stack[-1]