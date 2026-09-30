class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = 0
        L = 0
        avg = 1
        for R in range(len(arr)):
            print(f"L is {L} and R is {R}")
            avg *= arr[R]
            if (R - L) + 1 > k:
                avg /= arr[L]
                L += 1
            print(f"L is now {L} and R is {R}")
            if avg >= threshold:
                count += 1
        return count
            