class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = 0
        duplicates = set()
        for num in nums:
            if num in duplicates:
                return num
            duplicates.add(num)
        return num