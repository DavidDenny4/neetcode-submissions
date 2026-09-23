class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        min_val = 0
        while L <= R:
            mid = (L + R) // 2
            if (mid * mid) <= x:
                min_val = max(min_val, mid)
                L = mid + 1
            else:
                R = mid - 1
        return min_val
            