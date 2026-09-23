class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            if nums[L] <= nums[R]:
                return nums[L]
            
            mid = (L + R) // 2
            if nums[L] <= nums[mid]:
                L = mid + 1
            else:
                R = mid
        return nums[L]
        