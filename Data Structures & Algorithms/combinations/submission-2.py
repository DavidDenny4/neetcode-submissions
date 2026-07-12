class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(index, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return 
            
            if index > n:
                return 
                
            subset.append(index)
            helper(index + 1, subset)
            subset.pop()
            helper(index + 1, subset)

        helper(1, [])
        return res
