class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L, R = 1, max(piles)
        res = R
        while L <= R:
            mid = (L + R) // 2
            count = 0
            for p in piles:
                count += math.ceil(p // mid)
            if count <= h:
                res = min(res, mid)
                R = mid - 1
            else:
                L = mid + 1
        return res