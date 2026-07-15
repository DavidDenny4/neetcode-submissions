class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        print(f"nums is {nums}")
        sorted_nums = nums.sort()
        print(f"sorted_nums is {sorted_nums}")
        sorted_dec_nums = nums.sort(reverse=True)
        print(f"sorted_dec_nums is {sorted_dec_nums}")

        if sorted_nums == nums or sorted_dec_nums == nums:
            return True
        return False