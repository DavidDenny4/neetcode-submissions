class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if nums[L] <= nums[mid]:
                if target < nums[L] or target > nums[mid]:
                    L = mid + 1
                else:
                    R = mid
            else:
                if target > nums[R] or target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid
        
        return -1