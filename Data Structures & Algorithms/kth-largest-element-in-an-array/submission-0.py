class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            largest = heapq.heappop(nums)
            if i == k - 1:
                return largest
        return 0