from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import Topic



heaps = Topic(
    "Heaps",
    "",
    [],
    "", 
              [
    Problem(
        "3066",
        "Minimum Number of Operations to Exceed Threshold Value",
        '''You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

    Take the two smallest integers x and y in nums.
    Remove x and y from nums.
    Add min(x, y) * 2 + max(x, y) anywhere in the array.

Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.''',
        "https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/",
        "Medium",
        ["Arrays", "Min Heap"],
        [Example("nums = [2,11,10,1,3], k = 10", "2"), Example("nums = [1,1,2,4,9], k = 20", "4")],
        [Constraint("2 <= nums.length <= 2 * 10^5"), Constraint("1 <= nums[i] <= 10^9"), Constraint("1 <= k <= 10^9"), Constraint("The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to k.")],
        Solution(
            '''class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)

        while nums[0] < k:
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)

            newVal = (min1 * 2) + min2

            heapq.heappush(nums, newVal)
            res += 1
        return res''',
            "Anytime a problem talks about keeping track of the min element I think of using a min heap. Most of the time it's going to be faster overall to heapify and keep track of the heap as opposed to searching for the min on each iteration. This is each more true for this problem because we need two min values on every iteration. This problem is fairly simple when you see the min heap solution.",
            "O(nLogn)",
            "O(n)"
        )
    ),
    Problem(
        "295",
        "Find Median from Data Stream",
        '''The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
''',
        "https://leetcode.com/problems/find-median-from-data-stream/",
        "Hard",
        ["Design", "Heap"],
        [Example("", "")],
        [Constraint("")],
        Solution(
                '''class MedianFinder:

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
# param_2 = obj.findMedian()''',
                "For this problem I knew I wanted constant access to the middle of the stream at any point in time. This meant splitting it in two so you can always see the middle. To do this I use a min heap and a max heap. I push to the min heap to start. Then I push to the min heap if the num is less than the top of the min heap and to the max if its greater. If the heaps become unbalanced I move one value from the bigger heap to the smaller. To get the median, the heap with the extra value has the median. If the heaps are the same size then you can do the math to return the right value.",
                "O(logn)",
                "O(n)"
            )
    )
])