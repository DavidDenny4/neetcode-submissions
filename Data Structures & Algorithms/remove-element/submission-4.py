class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for R in range(len(nums)):
            if R != val:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        return nums[0:L + 1]