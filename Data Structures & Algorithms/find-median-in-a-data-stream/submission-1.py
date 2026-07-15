class MedianFinder:

    def __init__(self):
        smallest = []
        largest = []

    def addNum(self, num: int) -> None:
        # add to small max heap first
        heapq.heappush(smallest, -1 * num)
        if largest and -1 * smallest[0] > largest[0]:
            heapq.heappush(largest, -1 * heapq.heappop(smallest))
        # adjust if lengths differ 
        if len(smallest) > len(largest) + 1:
            heapq.heappush(largest, -1 * heapq.heappop(smallest))
        if len(largest) > len(smallest) + 1:
            heapq.heappush(smallest, -1 * heapq.heappop(largest))

    def findMedian(self) -> float:
        if len(smallest) > len(largest):
            return -1 * smallest[0]
        if len(largest) > len(smallest):
            return -1 * largest[0]
        return ((-1 * smallest[0]) + (largest[0])) / 2
        
        