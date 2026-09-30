class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[len(nums) - 1]]

        # Calculate prefix arrary
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i - 1])
        # Calculate postfix array
        for i in range(len(nums) - 2, 0, -1):
            postfix.insert(0, nums[i] * postfix[i + 1])

        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = postfix[0]
            elif i == len(nums) - 1:
                result[i] = prefix[i]
                break
            else:
                result[i] = prefix[i - 1] * postfix[i + 1]
        
        return result
        
