class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        valid = set()
        for num in nums:
            valid.add(num)
        for i in range(len(nums) + 1):
            if i not in valid:
                return i
        return 0
            
        