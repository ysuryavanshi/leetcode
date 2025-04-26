class MedianFinder:

    def __init__(self):
        self.data = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        idx = bisect_left(self.data, num)
        self.size += 1
        self.data.insert(idx, num)

    def findMedian(self) -> float:
        mid = self.size // 2
        if self.size % 2 == 0:
            return (self.data[mid] + self.data[mid - 1]) / 2
        return self.data[mid]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()