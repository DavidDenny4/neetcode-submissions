class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if target >= nums[L] and target < nums[mid]:
                R = mid
            elif target >= nums[mid] and target < nums[R]:
                L = mid
        return L
            
