class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = heapq.heapify([-num for num in nums])
        while len(self.heap) > k:
            heapq.heappop(heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
