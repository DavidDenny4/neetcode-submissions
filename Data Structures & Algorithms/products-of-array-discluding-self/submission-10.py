class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums)):
            last_index = len(nums) - 1
            if i == 0:
                postfix[last_index] = nums[last_index]
            else:
                postfix[last_index - i] = postfix[last_index - i + 1] * nums[last_index - i]

        result = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = postfix[i + 1]
            if i == len(nums) - 1:
                result[i] = prefix[i - 1]
            result[i] = prefix[i - 1] * postfix[i + 1]

        return result
        

