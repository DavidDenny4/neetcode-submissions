class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        
        count = 0
        sum, target = 0, k * threshold
        for i in range(k):
            sum += arr[i]
        if sum >= target:
            count += 1
        for i in range(k, len(arr)):
            sum -= arr[i - k]
            sum += arr[i]
            if sum >= target:
                count += 1
        return count