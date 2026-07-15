class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while max_heap:
            if len(max_heap) == 1:
                return -heapq.heappop(max_heap)
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)
            if second_largest > largest:
                heapq.heappush(maxheap, -(second_largest - largest))
        return 