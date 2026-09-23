class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        vals = sorted(list(map.values()))
        counts = vals[-k:]
        result = []
        for key in map:
            if map.get(key) in counts:
                result.append(key)
        return result