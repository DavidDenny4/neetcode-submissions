class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        visited = set()
        for i in range(len(nums)):
            # skip if we already checked with same value for first val
            if nums[i] in visited:
                continue
            
            L, R = i + 1, len(nums) - 1
            target = -nums[i]
            while L < R:
                if nums[L] + nums[R] > target:
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    results.append([nums[i], nums[L], nums[R]])
            visited.add(i)
        return results
            
        
            