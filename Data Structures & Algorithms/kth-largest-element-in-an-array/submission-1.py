class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_largest = [-num for num in nums]
        heapq.heapify(nums_largest)
        for i in range(k):
            largest = heapq.heappop(nums_largest)
            if i == k - 1:
                return largest
        return 0