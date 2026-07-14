class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L, R = 1, max(piles)
        res = R
        while L <= R:
            mid = (L + R) // 2
            print(f"L is {L}, R is {R}, mid is {mid}")
            count = 0
            for p in piles:
                print(f"p is {p}, going to add {math.ceil(p // mid)}")
                count += math.ceil(p // mid)
            print(f"count is {count}")
            if count <= h:
                res = min(res, mid)
                R = mid - 1
            else:
                L = mid + 1
        return res