class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence = 0
        for num in nums:
            count = 0
            # other number in set with continuous start
            if (num - 1) in nums_set:
                continue
            else:
                x = num
                while(x in nums_set):
                    count += 1
                    x += 1
                max_sequence = max(max_sequence, count)

        return max_sequence
            
