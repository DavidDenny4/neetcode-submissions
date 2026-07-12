class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L + 1, R + 1]
            if total < target:
                L += 1
            elif total > target:
                R -= 1
        
            