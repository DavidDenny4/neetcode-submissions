class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []
        for R in range(len(temperatures)):
            while stack and temperatures[R] > stack[-1][1]:
                L, temp = stack.pop()
                res[L] = R - L
            stack.append((R, temperatures[R]))
        print(f"res is {res}")
