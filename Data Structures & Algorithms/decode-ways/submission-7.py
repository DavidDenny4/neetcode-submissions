class Solution:
    def numDecodings(self, s: str) -> int:
        
        count = 0
        vals = [int(c) for c in s]
        print(f"vals is {vals} and s is {s}")
        for R in range(len(vals) - 1):
            if vals[R] in [1, 2] and vals[R + 1] in [1,2,3,4,5,6]:
                count += 1
            if vals[R] > 0:
                count += 1

