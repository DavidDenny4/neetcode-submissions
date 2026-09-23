class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3
        for color in nums:
            count[color] += 1
        
        index = 0
        for i in range(len(count)):
            for m in range(count[i]):
                nums[index] = i
                index += 1
        
        return
        