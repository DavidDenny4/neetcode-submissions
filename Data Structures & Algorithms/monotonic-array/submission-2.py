class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc_nums = nums.copy()
        desc_nums = nums.copy()
        asc_nums.sort()
        desc_nums.sort(reverse=True)
        print(f"asc: {asc_nums}")
        print(f"desc: {desc_nums}")        

        if sorted_nums == nums or sorted_dec_nums == nums:
            return True
        return False