class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        def checkSum(array, total):
            L, R = 0, len(array) - 1
            while L < R:
                if array[L] + array[R] > total:
                    R -= 1
                if array[L] + array[R] < total:
                    L += 1
                return [total,nums[L],nums[R]]
            return []

        for p1 in range(len(nums) - 2):
            window = nums[p1 + 1:]
            if checkSum(window, -p1):
                results.append(checkSum(window, -p1))
            return results
            