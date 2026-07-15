class MedianFinder:

    def __init__(self):
        self.smallest = []
        self.largest = []

    def addNum(self, num: int) -> None:
        # add to small max heap first
        heapq.heappush(self.smallest, -1 * num)
        if self.largest and -1 * self.smallest[0] > self.largest[0]:
            heapq.heappush(self.largest, -1 * heapq.heappop(self.smallest))
        # adjust if lengths differ 
        if len(self.smallest) > len(self.largest) + 1:
            heapq.heappush(self.largest, -1 * heapq.heappop(self.smallest))
        if len(self.largest) > len(self.smallest) + 1:
            heapq.heappush(self.smallest, -1 * heapq.heappop(self.largest))

    def findMedian(self) -> float:
        if len(self.smallest) > len(self.largest):
            return -1 * self.smallest[0]
        if len(self.largest) > len(self.smallest):
            return -1 * self.largest[0]
        return ((-1 * self.smallest[0]) + (self.largest[0])) / 2
        
        