class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = []
        for i in range(32):
            reverse.append(n & 1)
            n = n >> 1
        
        res = 0
        for m in range(32):
            res = res | (reverse.pop())
            res = res << 1
        return res