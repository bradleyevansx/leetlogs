## Find Median from Data Stream

**Difficulty**: `Hard` - **Tags**: `Design`, `Heap`

### Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


### Examples

**Example 1:**

**Input**: ``````

**Output**: ``````

### Constraints

- ``

### Solution

**Description**:

For this problem I knew I wanted constant access to the middle of the stream at any point in time. This meant splitting it in two so you can always see the middle. To do this I use a min heap and a max heap. I push to the min heap to start. Then I push to the min heap if the num is less than the top of the min heap and to the max if its greater. If the heaps become unbalanced I move one value from the bigger heap to the smaller. To get the median, the heap with the extra value has the median. If the heaps are the same size then you can do the math to return the right value.

**Time Complexity**: O(logn) - **Space Complexity**: O(n) 

**The Code:**

```python
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
```