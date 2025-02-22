class MedianFinder:

    def __init__(self):

        self.left = []
        self.lN = 0
        self.right = []
        self.rN = 0
        

    def addNum(self, num: int) -> None:
        if self.lN == 0:
            self.lN += 1
            self.left.append(-num)
            return
        if num <= 0-self.left[0]:
            heapq.heappush(self.left, -num)
            self.lN += 1
        else:
            heapq.heappush(self.right, num)
            self.rN += 1
        if not abs(self.lN - self.rN) > 1: return
        left = [-3, -2]
        right = []
        if self.lN > self.rN:
            maxL = -heapq.heappop(self.left)
            self.lN -= 1
            self.rN += 1
            heapq.heappush(self.right, maxL)
        else:
            minR = heapq.heappop(self.right)
            self.rN -= 1
            self.lN += 1
            heapq.heappush(self.left, -minR)

    def findMedian(self) -> float:
        if self.lN > self.rN:
            return -self.left[0]
        elif self.rN > self.lN:
            return self.right[0]
        else:
            return (self.right[0] - self.left[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()