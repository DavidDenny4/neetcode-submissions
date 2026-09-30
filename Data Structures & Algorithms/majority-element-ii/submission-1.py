class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count_map = Counter(nums)
        for key, count in count_map:
            if count > (len(nums) / 3):
                res.append(key)
        return res