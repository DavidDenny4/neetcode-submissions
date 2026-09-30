class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = []
        self.largest = k
        
        for n in nums:
            heapq.heappush(self.maxHeap, -1 * n)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap)

        stack = []
        for i in range(self.largest):
            stack.append(heapq.heappop(self.maxHeap))
        
        res = stack[-1]
        while stack:
            heapq.heappush(self.maxHeap, stack.pop())
        return -1 * res