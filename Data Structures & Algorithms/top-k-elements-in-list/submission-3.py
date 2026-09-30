class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        countList = []
        for key, val in countMap.items():
            countList.append(val, key)
        countList.sort()

        result = []
        for i in k:
            result.append(countList.pop())
        
        return result