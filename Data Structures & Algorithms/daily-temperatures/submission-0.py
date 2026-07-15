class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []
        for R in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                L, temp = stack.pop()
                res[L] = R - L
            stack.append((i, temperatures[i]))
        print(f"res is {res}")
