class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        
    def addNum(self, num: int) -> None:
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))

        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        else:
            return -self.low[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()