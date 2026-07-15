class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        for R in range(len(nums)):
            if nums[R] == nums[L]:
                if (R - L) <= k:
                    return True
                else:
                    L = R
        return False