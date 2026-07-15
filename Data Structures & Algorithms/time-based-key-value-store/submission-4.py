class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeVal = (timestamp, value)
        self.timeMap[key].append(timeVal)

    def get(self, key: str, timestamp: int) -> str:
        timeStamps = self.timeMap[key]
        if not timeStamps:
            return ""

        res = ""
        L, R = 0, len(timeStamps) - 1
        while L < R:
            mid = (R - L) // 2
            if timeStamps[mid][0] > timestamp:
                R = mid - 1
            else:
                res = timeStamps[mid][1]
                L = mid + 1
        return res
