class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return
            
            # add index to subset
            subset.append(nums[index])
            helper(index + 1, subset)
            subset.pop()

            # dont add index to subset
            while index < len(nums) - 2 and index[i] == index[i + 1]:
                index += 1
            helper(index + 1, subset)

        helper(0, [])
        return res