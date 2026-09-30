class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (R - L) // 2
            if nums[mid] == target:
                return mid
            if L == R:
                if target > nums[R]:
                    return R + 1
                else:
                    return L - 1    
            if target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
            